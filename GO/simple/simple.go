package main

import "fmt"
import "os"
import "log"
import "bufio"

func main(){
  scanner := bufio.NewScanner(os.Stdin)
  for scanner.Scan() {
    fmt.Println(scanner.Text())     
  }
  if err := scanner.Err(); err != nil {
    log.Println(err)
  }
}
