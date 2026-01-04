# モールス変換パッケージ
[![test](https://github.com/KaiKeiyama/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/KaiKeiyama/mypkg/actions/workflows/test.yml)
## 概要
- 文字をモールス信号に変換して配信します。

## 利用方法
次の手順で利用してください。

```
$ git clone git@github.com:KaiKeiyama/mypkg.git 
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash
``` 

## 使い方
- ローンチファイルを使用する場合

```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/kai69/.ros/log/2025-12-29-15-48-59-744285-kaipc-8497
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [8500]
[INFO] [listener-2]: process started with pid [8501]
[listener-2] [INFO] [1766990941.289169265] [listener_node]: Count:1 | Number:2
[listener-2] [INFO] [1766990942.261333806] [listener_node]: Count:2 | Number:3
[listener-2] [INFO] [1766990943.261567775] [listener_node]: Count:3 | Number:5
[listener-2] [INFO] [1766990944.263184764] [listener_node]: Count:4 | Number:7
[listener-2] [INFO] [1766990945.264527654] [listener_node]: Count:5 | Number:11
[listener-2] [INFO] [1766990946.261513817] [listener_node]: Count:6 | Number:13
[listener-2] [INFO] [1766990947.263352633] [listener_node]: Count:7 | Number:17
[listener-2] [INFO] [1766990948.262396245] [listener_node]: Count:8 | Number:19
[listener-2] [INFO] [1766990949.261215125] [listener_node]: Count:9 | Number:23
[listener-2] [INFO] [1766990950.263283574] [listener_node]: Count:10 | Number:29
```

## ２つの端末を使用する場合
### 端末１でtalkerを立ち上げる

```
ros2 run mypkg talker
```

### 端末２でlistenerを立ち上げる
- 素数を順番に出力する時
```
$ ros2 run mypkg listener
[INFO] [1766991542.666445444] [prime_listener]: Count:1 | Number:2
[INFO] [1766991543.665297643] [prime_listener]: Count:2 | Number:3
```

- 何番目の素数か出力する時

```
$ ros2 service call /get_nth_prime example_interfaces/srv/AddTwoInts "{a: 100}" #100番目の素数
waiting for service to become available...
requester: making request: example_interfaces.srv.AddTwoInts_Request(a=100, b=0)

response:
example_interfaces.srv.AddTwoInts_Response(sum=541) #541が100番目の素数である
```
# テスト環境
**OS**-Ubuntu 24.04

**ROS2**-Jazzy Jalisco

**Python**-3.12.3

# ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Kai Keiyama
