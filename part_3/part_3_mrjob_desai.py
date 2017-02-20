from mrjob.job import MRJob
from mrjob.step import MRStep
from collections import Counter
import itertools
import time

start_time = time.time()

class MRFriendYouMayKnow(MRJob):

    def mapper_connecteds_and_commons(self, _, line):
      minimum = -9999999999
      if '\t' not in line:
        line = line + '\t' + 'None' + line
      user, friends = line.split('\t')
      friends = friends.split(',')
      connecteds = [((user, friend), minimum) for friend in friends]
      commons = [(pair, 1) for pair in itertools.permutations(friends, 2)]
      return connecteds + commons

    def reducer_count_friends(self, pair, counts):
          yield pair, sum(counts)

    def mapper_filter_rearrange(self, pair, counts):
      if counts > 0:
          user, friend = pair[0], pair[1]
          yield user, [ (counts, friend) ] #wrap in List so it can be added to each other

    def reducer_groupByKey(self, key, values):     #groupByKey()
      yield key, list(itertools.chain(*values))    #yield key, reduce(lambda a, b: a + b, values)

    def mapper_suggestion(self, user, potentials):
      pairs = (int(user), dict((int(friend), count) for count, friend in potentials))
      sorted_results = (pairs[0], sorted(pairs[1].items(), key=lambda x: (-x[1], x))[:10])
      potential_friends = (sorted_results[0], [non_con[0] for non_con in sorted_results[1]])
      yield potential_friends[0], potential_friends[1]

    def steps(self):
      return [
            MRStep(mapper=self.mapper_connecteds_and_commons,
                       reducer=self.reducer_count_friends ),
            MRStep(mapper=self.mapper_filter_rearrange,
                       reducer=self.reducer_groupByKey ),
            MRStep(mapper=self.mapper_suggestion)]


if __name__ == '__main__':
      MRFriendYouMayKnow.run()

# print("--- %s seconds ---" % (time.time() - start_time))