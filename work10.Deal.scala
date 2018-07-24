import java.io.FileWriter

import scala.collection.mutable.ListBuffer

object Deal {
  def main(args: Array[String]): Unit = {
    import org.json.JSONObject
    import org.apache.spark.SparkConf
    import org.apache.spark.SparkContext
    val conf = new SparkConf().setAppName("cala").setMaster("local")
    val sc = new SparkContext(conf)
    val ls = sc.textFile("all_data_4.txt")


      .filter(line=>line.endsWith("status\":1}"))
      .flatMap(line=>{
        val json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        val list = ListBuffer[JSONObject]()
        for(i<-0 to jsonlist.length()-1){
          list.append(jsonlist.getJSONObject(i))
        }
        list

      })

      .map(line=>(line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
//      .foreach(line=>println(line))
      .take(2300)
    val writer = new FileWriter("group4_data2.txt")
    for(i<-0 to ls.length-1){
      writer.write(ls(i)._2+",")
  }
    writer.close()
  }
}

