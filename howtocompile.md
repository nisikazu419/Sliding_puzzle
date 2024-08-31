# prerequisite
以下を確認  
- gcc or clangが入っている  
つまり、以下のどちらかが動作すれば良い  
```bash
$g++ --version
or
$clang++ --version
```
# compile
上記で動作したほうで、  
```bash
$g++ -std=c++2b main.cpp
or
$clang++ -std=c++2b main.cpp
```

# execution
```bash
./a.out 2>/dev/null 1>list.txt
```
---ここまで動作確認済み---  
---ここから未確認---
その後、エクセルに変換  
```bash
python convert.py
```

# why so slow?
プログラムを実行したら、ランダムに生成する部分にめっちゃ時間かかってる。

一応、2>/dev/nullを外すと、generating...とgenerated!が出るから見てみて。
