# 求人ボックス スクレイピングツール（Python × Playwright）

## 📌 概要
- 本ツールは、求人検索サイト「求人ボックス」から「東京都 × プログラマー」の求人情報を**2ページ分**スクレイピングし、Excelファイルとして出力します。
- ポートフォリオ作品として作成しました。

## 🛠️ 技術スタック
- Python 3.10+
- Playwright（非同期・動的ページ対応）
- pandas / openpyxl（Excel出力）

## 🎯 主な機能
- 求人リストページから企業ごとの詳細ページURLを抽出
- 各ページにアクセスして下記の項目を取得：
  - 【求人タイトル】
  - 【企業名】
  - 【所在地】
  - 【給与】
  - 【雇用形態】
- 取得結果をExcel（求人情報一覧.xlsx）に出力
- `N/A` は空セルとして扱い、データの整形に配慮

## 💻 実行方法

### 1. ライブラリのインストール

```bash
pip install playwright pandas openpyxl
playwright install
```

### 2. スクリプトを実行

```bash
python main.py
```

実行後、カレントディレクトリに `求人情報一覧.xlsx` が出力されます。

## 📂 出力例（Excel）

| 求人タイトル           | 企業名         | 所在地       | 給与         | 雇用形態   |
|----------------------|----------------|--------------|--------------|------------|
| Pythonエンジニア募集 | 株式会社ABC     | 東京都新宿区 | 月給30万円〜 | 正社員     |
| Web開発スタッフ      | 株式会社XYZ     | 東京都港区   | 時給1500円〜 | アルバイト |

## 🧭 今後の展望
- 全ページへのページネーション対応（現在は2ページのみ）
- Webアプリ（Flask）版への拡張
- 重複排除や検索条件入力フォームの追加

## ✍ 作者
- 名前：Rin Nakahata
- 技術ブログ（note）：[note記事はこちら](https://note.com/rin_nakahata/n/n82436c323c5c)

## 📄 ライセンス
MIT License
