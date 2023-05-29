import matplotlib.colors as mcolors


class AnsiCreateImage:
    str1 = "\033[48;5;"
    str2 = "m  \033[0m"

    def __init__(self):
        self.min_parameter = 0
        self.pixel_count = 0
        self.different_min = 1000

    def ansi_create_4bit(self):
        ansi_4bit = [
            "#000000",
            "#aa0000",
            "#00aa00",
            "#aaaa00",
            "#0000aa",
            "#aa00aa",
            "#00aaaa",
            "#aaaaaa",
            "#555555",
            "#ff5555",
            "#55ff55",
            "#ffff55",
            "#5555ff",
            "#ff55ff",
            "#55ffff",
            "#ffffff"
        ]

        ansi_4bit_RGB = []
        for color_name in ansi_4bit:
            ansi_4bit_RGB.append(tuple(int(c * 255) for c in mcolors.to_rgb(color_name)))
        return ansi_4bit_RGB

    def ansi_create_8bit(self):
        ansi_8bit_parts = ["00", "5f", "87", "af", "d7", "ff"]

        ansi_8bit = [
            "#000000",
            "#800000",
            "#008000",
            "#808000",
            "#000080",
            "#800080",
            "#008080",
            "#c0c0c0",
            "#808080",
            "#ff0000",
            "#00ff00",
            "#ffff00",
            "#0000ff",
            "#ff00ff",
            "#00ffff",
            "#ffffff"
        ]

        for parts_red in ansi_8bit_parts:
            for parts_green in ansi_8bit_parts:
                for parts_blue in ansi_8bit_parts:
                    ansi_8bit.append("#" + parts_red + parts_green + parts_blue)

        ansi_8bit.append("#080808")
        ansi_8bit.append("#121212")
        ansi_8bit.append("#1c1c1c")
        ansi_8bit.append("#262626")
        ansi_8bit.append("#303030")
        ansi_8bit.append("#3a3a3a")
        ansi_8bit.append("#444444")
        ansi_8bit.append("#4e4e4e")
        ansi_8bit.append("#585858")
        ansi_8bit.append("#626262")
        ansi_8bit.append("#6c6c6c")
        ansi_8bit.append("#767676")

        ansi_8bit.append("#808080")
        ansi_8bit.append("#8a8a8a")
        ansi_8bit.append("#949494")
        ansi_8bit.append("#9e9e9e")
        ansi_8bit.append("#a8a8a8")
        ansi_8bit.append("#b2b2b2")
        ansi_8bit.append("#bcbcbc")
        ansi_8bit.append("#c6c6c6")
        ansi_8bit.append("#d0d0d0")
        ansi_8bit.append("#dadada")
        ansi_8bit.append("#e4e4e4")
        ansi_8bit.append("#eeeeee")

        ansi_8bit_RGB = []
        for color_name in ansi_8bit:
            ansi_8bit_RGB.append(tuple(int(c * 255)for c in mcolors.to_rgb(color_name)))
        return ansi_8bit_RGB

    def f_conversion_4bit(self, pixel_img, filename):

        height, width = pixel_img.shape[:2]

        # ANSIエスケープシーケンスが表せる16色のそれぞれのRGB値を登録
        ansi_RGB = self.ansi_create_4bit()

        # smallest_difference_image_ANSI_RGB = []
        count = 0
        different_sum = 0

        self.str1 = "\033["
        self.str2 = "m  \033[0m"

        # try:
        with open(filename, 'w') as f:
            for x in range(0, height):
                for y in range(0, width):
                    for z in ansi_RGB:
                        different_sum += abs(pixel_img[x, y, 0] - z[0])
                        different_sum += abs(pixel_img[x, y, 1] - z[1])
                        different_sum += abs(pixel_img[x, y, 2] - z[2])
                        if (different_sum < self.different_min):
                            self.different_min = different_sum
                            self.min_parameter = count
                        count += 1
                        different_sum = 0
                    if (self.min_parameter <= 7):
                        self.min_parameter += 100
                    else:
                        self.min_parameter += 92
                    f.write(self.str1 + str(self.min_parameter) + self.str2)
                    self.ANSI_information(pixel_img, ansi_RGB, x, y)
                    self.different_min = 1000
                    self.pixel_count += 1
                    count = 0
                print()
                f.write("\n")

    def f_conversion_8bit(self, pixel_img, filename):
        height, width = pixel_img.shape[:2]

        # ANSIエスケープシーケンスが表せる256色のそれぞれのRGB値を登録
        ansi_RGB = self.ansi_create_8bit()

        count = 0
        different_sum = 0

        self.str1 = "\033[48;5;"
        self.str2 = "m  \033[0m"

        try:
            with open(filename, 'w') as f:
                for x in range(0, height):
                    for y in range(0, width):
                        for z in ansi_RGB:
                            different_sum += abs(pixel_img[x, y, 0] - z[0])
                            different_sum += abs(pixel_img[x, y, 1] - z[1])
                            different_sum += abs(pixel_img[x, y, 2] - z[2])
                            if (different_sum < self.different_min):
                                self.different_min = different_sum
                                self.min_parameter = count
                            count += 1
                            different_sum = 0
                        f.write(self.str1 + str(self.min_parameter) + self.str2)
                        self.ANSI_information(pixel_img, ansi_RGB, x, y)
                        self.different_min = 1000
                        self.pixel_count += 1
                        count = 0
                    print()
                    f.write("\n")
        except Exception:
            print("テキストファイル書き込みに失敗しました。")

    def ANSI_information(self, pixel_img, ansi_RGB, x, y):
        print(f"色:{self.str1 + str(self.min_parameter) + self.str2}", end='  ')
        print(f"ピクセル数:{self.pixel_count}", end="  ")
        print(f"元RGB:{pixel_img[x, y, :]}", end="  ")
        print(f"登録ANSI:{self.min_parameter}", end="  ")
        print(f"登録RGB:{ansi_RGB[self.min_parameter]}", end="  ")
        print(f"誤差:{self.different_min}")