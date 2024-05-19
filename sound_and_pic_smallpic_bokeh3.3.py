from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, CustomJS, TapTool, Circle, HoverTool
import base64
from PIL import Image
from io import BytesIO

def encode_image(file_path, format='WEBP', size=(224, 224), quality=75):
    # 画像を開く
    img = Image.open(file_path)
    # リサイズ
    img = img.resize(size, Image.LANCZOS)
    # BytesIOを使用してメモリ上に保存
    buffer = BytesIO()
    img.save(buffer, format=format, quality=quality)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

def encode_audio(file_path):
    # 音声ファイルを開く
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

# 音声データと画像データをBase64でエンコード
audio_files = ["test1.mp3", "test2.mp3", "test3.mp3"]
image_files = ["test1.png", "test2.png", "test3.png"]
encoded_audios = [encode_audio(f"./{f}") for f in audio_files]
encoded_images = [encode_image(f"./{f}", format='WEBP', size=(124, 124), quality=30) for f in image_files]

# Bokehのプロットを設定 boke2:plot_width -> boke3:width
p = figure(width=800, height=800, tools="tap,pan, wheel_zoom, reset")

# データソースの設定
source = ColumnDataSource(data={
    'x': [1, 2, 3],
    'y': [4, 5, 6],
    'audio': encoded_audios,
    'image': encoded_images  # 画像データを追加
})

# サークルの描画設定
circle_renderer = p.circle('x', 'y', size=20, source=source, color='navy', selection_color='green')

# 選択されていない時のスタイルを明示的に設定
nonselection_circle = Circle(fill_color='navy', line_color='navy')
circle_renderer.nonselection_glyph = nonselection_circle

# CustomJSを使って音声を再生するコード
code = """
    var indices = source.selected.indices;
    if (indices.length > 0) {
        var audio_src = source.data['audio'][indices[0]];
        if (window.audio_player) {
            window.audio_player.pause();  // 前の音声を停止
        }
        window.audio_player = new Audio("data:audio/mp3;base64," + audio_src);
        window.audio_player.play();  // 新しい音声を再生
    }
"""
taptool = p.select(type=TapTool)
taptool.callback = CustomJS(args=dict(source=source), code=code)

# HoverToolの設定で画像サムネイルを表示
hover = HoverTool(tooltips="""
    <div>
        <div><strong>Point:</strong> @x, @y</div>
        <div><img src="data:image/webp;base64,@image" width="100" height="100" style="float: left; margin: 0 15px 15px 0;" alt="Image not available"></div>
    </div>
""")
p.add_tools(hover)

output_file("interactive_graph_with_sound_images.html")
show(p)
