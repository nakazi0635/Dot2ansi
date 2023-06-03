# dot2ansi
(Introduction: The README on GitHub may be incomplete. Please be aware of this.)

ANSI escape sequences can be used to
You can color the output of the terminal or rewrite the output.

This time, we created a program to convert a dot picture to ANSI escape code on a Mac and have it drawn on a terminal

# DEMO

<img width="399" alt="スクリーンショット 2023-06-01 19 35 38" src="https://github.com/nakazi0635/dot2ansi/assets/91645661/4d8ace50-0999-45d6-8c0c-080eff0bffdb">



# Features

Examines a dot picture pixel by pixel and calculates RGB values.

Finds the color with the smallest error in RGB value from the colors that can be represented by ANSI escape code.
<img width="653" alt="print1" src="https://github.com/nakazi0635/dot2ansi/assets/91645661/1e454c7d-fa20-49f3-b39e-7d29f4f1689d">

Outputs the colors found in this way to a text file.
<img width="855" alt="print2" src="https://github.com/nakazi0635/dot2ansi/assets/91645661/a35715f7-6891-4e1b-9723-064960f46ce0">

Change the terminal to zsh and specify a shell split to be executed after the terminal is started to achieve drawing.

# Requirements.

* Python 3.11.3
* Pillow 9.5.0
* numpy 1.24.3
* cv2 4.7.0
* tkinter 8.6
* matplotlib 3.7.1

# Installed

```zsh
pip install pillow
pip install matplotlib
```

# Usage

## Create ANSI escape code

Install the above library.

Prepare a dot picture of about 30 x 30 pixels. (For example, you can use the ipad app dotpict to create one.)

Clone this repository.

Execute "Img_input.py".

Open the dotpict image you created from the file dialog.

Press save in 256 colors from the file dialog.

Save the generated text file.

## Draw a dot picture in the terminal.

Let's type the command zsh_1

```zsh_1
echo $SHELL
```

If you see /bin/zsh instead of /bin/bash, skip this section.

```zsh_2
chsh -s /bin/zsh
```

After entering the zsh_2 command, enter zsh_1 again and see if it shows up as /bin/zsh.

```zsh_3
open ~/.zshrc
```

Then enter zsh_3 and open the configuration file with text.

Rewrite the configuration file as follows.

*The following assumes that dot2ansi is cloned directly under the home directory. Please change it so that the path goes through the cloned repository file.

```zsh_4
cd ~/dot2ansi/
zsh random_Print.sh
cd ... /. 
```

The following shell splict is written in single_Print.shell.
Replace the path to AA1 with the path to the text file that converts the dot pictures to ANSI escape codes.

```single_Print.shell
paint_terminal_animation() {
    AA1="sed -e 's/^/\t/g' ~/dot2ansi/kirby.txt" 
    eval $AA1 
}
paint_terminal_animation
```

That's all for configuration. If the prepared dot picture is displayed when you start the terminal, it is success.

# Caution.

Linux and Windows environments have not been tested.

# Author.

* Naka

# License

"ANSI escape sequences" can be found under [ANSI escape sequences](https://en.wikipedia.org/wiki/ANSI_escape_code#External_links).

Let the terminal display the dots!

Thank you very much!
