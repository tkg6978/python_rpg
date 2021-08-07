
from enum import Enum

from event import Event
from text import Text


KEY_LIST = {
    'up': ['w', 'W', 'ｗ', 'Ｗ'],
    'down': ['s', 'S', 'ｓ', 'Ｓ'],
    'left': ['a', 'A', 'あ', 'Ａ'],
    'right': ['d', 'D', 'ｄ', 'Ｄ'],
    'esc': ['q', 'Q', 'ｑ', 'Ｑ'],
    'item': ['e', 'E', 'え', 'E'],
    'help': ['x', 'X', 'ｘ', 'Ｘ'],
}
MAP = [
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['B', 'P', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'H', 'E', 'E', 'E', 'H', 'B'],
    ['B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
    ['B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'B'],
    ['B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'B'],
    ['B', 'H', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'B'],
    ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'B'],
    ['B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'B'],
    ['B', 'E', 'S', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'B'],
    ['B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
    ['B', 'E', 'E', 'E', 'E', 'H', 'B', 'W', 'E', 'E', 'E', 'E', 'B', 'E', 'H', 'E', 'E', 'E', 'G', 'B'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
]
HP_FORMAT = ' HP:[{}/{}] '


class Map:
    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, value):
        self._counter = value

    @property
    def now_h(self):
        return self._now_h

    @now_h.setter
    def now_h(self, value):
        self._now_h = value

    @property
    def now_w(self):
        return self._now_w

    @now_w.setter
    def now_w(self, value):
        self._now_w = value

    @property
    def goal_flg(self):
        return self._goal_flg

    @goal_flg.setter
    def goal_flg(self, value):
        self._goal_flg = value

    @property
    def game_over_flg(self):
        return self._game_over_flg

    @game_over_flg.setter
    def game_over_flg(self, value):
        self._game_over_flg = value

    @property
    def show_item_flg(self):
        return self._show_item_flg

    @show_item_flg.setter
    def show_item_flg(self, value):
        self._show_item_flg = value

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, value):
        self._field = value

    def __init__(self):
        self._now_h = 1
        self._now_w = 1
        self._counter = 0
        self._goal_flg = False
        self._game_over_flg = False
        self._show_item_flg = False
        self._field = ''

    def show(self):
        """マップを表示
        """
        Event.clear()
        print(Text.MES_HOW_TO_PLAY)

        # 二次元配列の文字列を、コマンドライン表示用に変換
        for array in MAP:
            map = ''
            for string in array:
                map = map + MapItem(string).map_item
            print(map)

    def move(self):
        """マップを移動
        """
        while True:
            # 移動先フィールドを初期化
            self.field = ''
            input_key = input()

            # 終了
            if input_key in KEY_LIST['esc']:
                self.game_over_flg = True
                break

            # アイテム一覧
            elif input_key in KEY_LIST['item']:
                self.show_item_flg = True
                break

            # 下へ
            if input_key in KEY_LIST['down']:
                next_height = self.now_h + 1
                self.change_field(next_height, self.now_w)

            # 左へ
            elif input_key in KEY_LIST['left']:
                next_width = self.now_w - 1
                self.change_field(self.now_h, next_width)

            # 右へ
            elif input_key in KEY_LIST['right']:
                next_width = self.now_w + 1
                self.change_field(self.now_h, next_width)

            # 上へ
            elif input_key in KEY_LIST['up']:
                next_height = self.now_h - 1
                self.change_field(next_height, self.now_w)

            # 不正な入力の場合
            else:
                print(Text.MES_CAN_NOT_USE_KEY)
                continue

            # 移動先フィールドが壁の場合
            if self.field == MapItem.BLOCK.value:
                continue

            self.counter += 1
            break

    def change_field(self, height, width):
        """フィールドを更新
        """
        # ゴールの場合
        if MAP[height][width] == MapItem.GOAL.value:
            self.goal_flg = True

        # 空地の場合
        elif MAP[height][width] == MapItem.EMPTY.value:
            self._change_field(height, width)

        # 剣の場合
        elif MAP[height][width] == MapItem.WEAPON.value:
            self._change_field(height, width)

            self.field = MapItem.WEAPON.value

        # 盾の場合
        elif MAP[height][width] == MapItem.SIELD.value:
            self._change_field(height, width)

            self.field = MapItem.SIELD.value

        # 薬の場合
        elif MAP[height][width] == MapItem.HERBS.value:
            self._change_field(height, width)

            self.field = MapItem.HERBS.value

        else:
            self.field = MapItem.BLOCK.value
            input(Text.MES_CAN_NOT_MOVE)

    def _change_field(self, height, width):
        # 現在位置を空地へ
        MAP[self.now_h][self.now_w] = MapItem.EMPTY.value

        # 移動先をPへ
        if height > self.now_h:
            MAP[self.now_h + 1][self.now_w] = MapItem.PLAYER.value
            self.now_h += 1
        elif height < self.now_h:
            MAP[self.now_h - 1][self.now_w] = MapItem.PLAYER.value
            self.now_h -= 1
        elif width > self.now_w:
            MAP[self.now_h][self.now_w + 1] = MapItem.PLAYER.value
            self.now_w += 1
        elif width < self.now_w:
            MAP[self.now_h][self.now_w - 1] = MapItem.PLAYER.value
            self.now_w -= 1


class MapItem(str, Enum):
    """マップアイテム一覧
    """
    def __new__(cls, value, map_item, title, description):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.map_item = map_item
        obj.title = title
        obj.description = description
        return obj

    BLOCK = 'B', '＃', '壁', '侵入不可エリア（壁）'
    EMPTY = 'E', '　', '空地', '何もないフィールド'
    PLAYER = 'P', 'P ', 'プレイヤー', 'プレイヤーの現在位置'
    GOAL = 'G', 'G ', 'ゴール', 'ゴールの位置'
    WEAPON = 'W', '剣', '勇者の剣', '武器/勇者の剣/持っているだけで攻撃力アップ：'
    SIELD = 'S', '盾', '勇者の盾', '防具/勇者の盾/持っているだけで防御力アップ'
    HERBS = 'H', '薬', '薬草', '道具/薬草/使うとHPがすこし回復する'
