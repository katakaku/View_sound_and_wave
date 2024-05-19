## プログラムの概要
- **目的**: 音声と画像を含むインタラクティブなグラフをWebブラウザで表示する。
- **使用技術**: Python, Bokeh, PIL, Base64エンコーディング。

## 機能詳細

### 1. Base64エンコーディング
#### `encode_image`関数:
- **入力**: `file_path` (画像ファイルパス), `format` (保存フォーマット, デフォルトは'WEBP'), `size` (画像サイズ, デフォルトは224x224ピクセル), `quality` (画像品質, デフォルトは75)
- **処理**:
  - 指定されたファイルパスから画像を読み込む。
  - 画像をリサイズし、指定されたフォーマットと品質で保存する。
  - 画像をBase64形式にエンコードして返す。
#### `encode_audio`関数:
- **入力**: `file_path` (音声ファイルパス)
- **処理**:
  - 指定されたファイルパスから音声ファイルを読み込み、Base64形式にエンコードして返す。

### 2. Bokehグラフ設定
- **プロットの設定**:
  - サイズは800x800ピクセル。利用可能なツールにはタップ、パン、ズーム、リセットが含まれる。
- **データソース**:
  - X、Y座標およびエンコードされた音声・画像データを持つ。
- **ビジュアル表現**:
  - サークルを使用してポイントを描画。選択時と非選択時の色を設定。
- **インタラクティブ機能**:
  - **タップツール**:
    - ポイントをタップすると、そのポイントに関連付けられた音声が再生される。
  - **ホバーツール**:
    - ポイントにマウスをホバーすると、関連付けられた画像のサムネイルが表示される。

### 3. 出力
- **出力ファイル**: "interactive_graph_with_sound_images.html"としてHTMLファイルを出力。
- **表示**: Bokehサーバーを通じてHTMLファイルがブラウザで開かれる。
