# mini project

ミニプロでは「フィギュアスケートのジャンプにおけるエッジエラー判定の自動化」をテーマに研究を進める。  
対象のジャンプは1Lz(single Lutz)。用いたデータセットやソースコードをここに公開する。

データ収集にはNOITOM社製慣性センサ [perceotion neuron 3.0](https://neuronmocap.com/pages/perception-neuron-3) を用いた。

# モーションキャプチャの様子

専用ソフト"Axis studio"におけるキャプチャ画面を以下に示す。  
キャプチャファイルはbvh形式にてexportされる。

![67c48197-47f7-4171-b366-c166f64ee0ba](https://user-images.githubusercontent.com/102862947/188489734-987cae8c-3a9c-4610-b219-0fd4ad2da1a7.gif)

# bvhtoolbox

bvh形式にてexportされたファイルを、[bvhtoolbox](https://pypi.org/project/bvhtoolbox/)を用いてcsv形式に変換した。  

インストールは  
```pip install bvhtoolbox```  
で行う。  

csv形式への変換は、  
```bvh2csv import.bvh```  
というコマンドを用いて行う。  
入力のbvhデータは、positionデータとrotaitionデータの2つのcsvファイルに分けて出力される。

# Note

データセット作成中…。

# Author

* 作成者：田中諒汰
* 所属：名古屋大学工学部電気電子情報工学科　武田研究室
* E-mail：tanaka.ryota@g.sp.m.is.nagoya-u.ac.jp
