import argparse
import textwrap

class ArgsHelpFormat(
    argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawTextHelpFormatter
):
    pass

def argumentParse():
    parse = argparse.ArgumentParser(
        description='宝くじ分析 (Takarakuji Analysis)',
        formatter_class=ArgsHelpFormat,
        epilog=textwrap.dedent(
            """
            宝くじ分析 追加情報：
                このプログラムは完全な予測を目的にしているのではなく，勝率を上げるために作成された．
                決してこのプログラムを鵜呑みにしないでください．
                
            各種目確立一覧：
                NUMBERS3：
                            [0~9][0~9][0~9] = 3^9 = 19,680 通り
                            1口： 200 yen
                            Total: 19,680 x 200 = 3,936,000 yen
                            Target 126: 126 x 200 = 25,200 yen | Dream: 100,000 yes DIFF: 100,000 - 25,200 = 74,800 yen
                NUMBERS4：
                            [0~9][0~9][0~9][0~9] = 4^9 = 262,144 通り
                            1口： 200 yen
                            Total: 262,144 x 200 = 52,428,800 yen
                            Target 126: 126 x 200 = 25,200 yen | Dream: 1,000,000 yes DIFF: 1,000,000 - 25,200 = 974,800 yen
                MINILOT ：
                            [?][?][?][?][?] (0~31) = 31C5 = 169,911 通り
                            1口： 200 yen
                            Total: 169,911 x 200 = 33,982,200 yen
                            Target 126: 126 x 200 = 25,200 yen | Dream: 10,000,000 yes DIFF: 10,000,000 - 25,200 = 9,974,800 yen
                LOT6    ：
                            [?][?][?][?][?][?] (0~43) = 43C6 = 6,096,454 通り
                            1口： 200 yen
                            Total: 6,096,454 x 200 = 1,219,290,800 yen
                            Target 126: 126 x 200 = 25,200 yen | Dream: 600,000,000 yes DIFF: 600,000,000 - 25,200 = 599,974,800 yen
                LOT7    ：
                            [?][?][?][?][?][?][?] (0~37) = 37C7 = 10,295,472 通り
                            1口： 300 yen
                            Total: 10,295,472 x 300 = 3,088,641,600 yen
                            Target 126: 126 x 300 = 37,800 yen | Dream: 1,000,000,000 yes DIFF: 1,000,000,000 - 25,200 = 999,974,800 yen
                
            """
        )
    )

    # parse.add_argument('--aaa', default='aaaa', type=str, help='?')

    subparsers = parse.add_subparsers()

    checksite = subparsers.add_parser(
        name='checksite (更新情報の確認及び更新)',
        formatter_class=ArgsHelpFormat,
        help=textwrap.dedent("""
        (checksite) 更新情報の確認及び更新
            help: -h --help
            -c, --check (最新情報確認)
            -u, --update (最新情報更新)
            -v, --verbose (最新情報表示)

        """)
    )
    checksite.add_argument('-c', '--check', action='store_true', help='最新情報確認')
    checksite.add_argument('-u', '--update', action='store_true', help='最新情報更新')
    checksite.add_argument('-v', '--verbose', action='store_true', help='最新情報表示')

    analyze = subparsers.add_parser(
        name='analyze (更新情報の分析)',
        formatter_class=ArgsHelpFormat,
        help=textwrap.dedent("""
        (analyze) 分析の実行
            help: -h --help
            -r, --run (実行)

        """)
    )
    analyze.add_argument('-r', '--run', action='store_true', default='実行')

    schedulebuy = subparsers.add_parser(
        name='schedulebuy (時間指定チケット購入)',
        formatter_class=ArgsHelpFormat,
        help=textwrap.dedent("""
        (schedulebuy) 時間指定チケット購入
            help: -h --help

        """)
    )

    return parse.parse_args()

if __name__ == '__main__':
    print(argumentParse())