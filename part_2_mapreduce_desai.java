// package: identifies what the Java program belongs to
package edu.wm.lettercount;

import java.io.IOException;
import java.util.Arrays;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;


// public anyone can access
public class LetterCount extends Configured implements Tool {
   public static void main(String[] args) throws Exception {
      System.out.println(Arrays.toString(args));
      int res = ToolRunner.run(new Configuration(), new LetterCount(), args);

      System.exit(res);
   }

   @Override
   public int run(String[] args) throws Exception {
      System.out.println(Arrays.toString(args));
      Job job = new Job(getConf(), "LetterCount");
      job.setJarByClass(LetterCount.class);
      job.setOutputKeyClass(Text.class);
      job.setOutputValueClass(IntWritable.class);

      job.setMapperClass(Map.class);
      job.setReducerClass(Reduce.class);

      job.setInputFormatClass(TextInputFormat.class);
      job.setOutputFormatClass(TextOutputFormat.class);

      FileInputFormat.addInputPath(job, new Path(args[0]));
      FileOutputFormat.setOutputPath(job, new Path(args[1]));

      job.waitForCompletion(true);

      return 0;
   }

//  trying to look at the first letter
   public static class Map extends Mapper<LongWritable, Text, Text, IntWritable> {
//      private final static IntWritable ONE = new IntWritable(1);
    //  changed the var to letter and takes 1 byte characters
//      private Text result = new Text();

//      @Override
      public void map(LongWritable key, Text value, Context context)
              throws IOException, InterruptedException {
// maybe use something with this? .charAt(0)
         for (String token: value.toString().split("\\s+")) {
            // word.set(token);
            // I think this assigns the var letter to token
        	String word = token.toString();
        	String letter = word.substring(0,1);
//            char[] letters = word.toCharArray();
//            char letter = word.charAt(0);
//            String letter = Character.toString(first_let);
//            result.set(letter);
            // context.write(word, ONE);
        	System.out.println(token);
        	System.out.println(letter);
            context.write(new Text(letter), new IntWritable(1));
         }
      }
   }

   public static class Reduce extends Reducer<Text, IntWritable, Text, IntWritable> {
      @Override
      public void reduce(Text key, Iterable<IntWritable> values, Context context)
              throws IOException, InterruptedException {
         int sum = 0;
         IntWritable result = new IntWritable();
         for (IntWritable val : values) {
            sum += val.get();
            result.set(sum);
         }
         System.out.println(result);
         context.write(key, result);
      }
   }
}
