/**
  * Created by apple on 2018/7/20.
  */
import scala.util.control.Breaks._
object Temp {
  def main(args: Array[String]) {
    var temp = List(38, 39, 37, 37, 35)
    var l = temp.length
    for (i <- Range(0, l)) {
      breakable {
        if (i == 2) {
          println("星期三：" + temp(i))
          break()
        }
        println(temp(i))
      }
    }
  }
}