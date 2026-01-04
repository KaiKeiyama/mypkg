# モールス変換パッケージ
[![test](https://github.com/KaiKeiyama/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/KaiKeiyama/mypkg/actions/workflows/test.yml)
## 概要
- 文字をモールス信号に変換して配信します。アルファベットと数字にのみ可能です。
## 使い方
- デフォルトの文字(SOS)をモールス信号に変換する場合

```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/kai69/.ros/log/2026-01-04-14-51-44-904155-kaipc-3405
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [3408]
[INFO] [listener-2]: process started with pid [3409]
[listener-2] [INFO] [1767505906.572580937] [listener]: Received: SOS -> Morse: ... --- ...
[listener-2] [INFO] [1767505907.555477260] [listener]: Received: SOS -> Morse: ... --- ...
[listener-2] [INFO] [1767505908.555968186] [listener]: Received: SOS -> Morse: ... --- ...
[listener-2] [INFO] [1767505909.555723922] [listener]: Received: SOS -> Morse: ... --- ...
[listener-2] [INFO] [1767505910.555872077] [listener]: Received: SOS -> Morse: ... --- ...
[listener-2] [INFO] [1767505911.555696388] [listener]: Received: SOS -> Morse: ... --- ...
```

- 文字を変更(OUTOUSEYO)してモールス信号に変換する場合

```
[INFO] [launch]: All log files can be found below /home/kai69/.ros/log/2026-01-04-14-57-39-522577-kaipc-3500
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [3503]
[INFO] [listener-2]: process started with pid [3504]
[listener-2] [INFO] [1767506261.132413697] [listener]: Received: OUTOUSEYO -> Morse: --- ..- - --- ..- ... . -.-- ---
[listener-2] [INFO] [1767506262.114201821] [listener]: Received: OUTOUSEYO -> Morse: --- ..- - --- ..- ... . -.-- ---
[listener-2] [INFO] [1767506263.114147222] [listener]: Received: OUTOUSEYO -> Morse: --- ..- - --- ..- ... . -.-- ---
[listener-2] [INFO] [1767506264.113886352] [listener]: Received: OUTOUSEYO -> Morse: --- ..- - --- ..- ... . -.-- ---
[listener-2] [INFO] [1767506265.113252686] [listener]: Received: OUTOUSEYO -> Morse: --- ..- - --- ..- ... . -.-- ---
[listener-2] [INFO] [1767506266.113322110] [listener]: Received: OUTOUSEYO -> Morse: --- ..- - --- ..- ... . -.-- ---
```
# テスト環境
**OS**:Ubuntu 24.04

**ROS2**:Jazzy Jalisco

**Python**:3.12.3

# ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Kai Keiyama
