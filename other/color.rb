#!/usr/bin/env ruby

#黒色
def black2
  print "\033[",100.to_s, "m","  \033[0m"
end
#灰色
def black
  print "\033[", 40.to_s, "m","  \033[0m"
end

#白色、灰色
def red2
  print "\033[",101.to_s, "m","  \033[0m"
end
def red
  print "\033[", 41.to_s, "m","  \033[0m"
end

# #白色、灰色
# def white
#   print "\033[",102.to_s, "m","  \033[0m"
# end
# def gray
#   print "\033[", 42.to_s, "m","  \033[0m"
# end

# #白色、灰色
# def white
#   print "\033[",103.to_s, "m","  \033[0m"
# end
# def gray
#   print "\033[", 43.to_s, "m","  \033[0m"
# end

# #白色、灰色
# def white
#   print "\033[",104.to_s, "m","  \033[0m"
# end
# def gray
#   print "\033[", 44.to_s, "m","  \033[0m"
# end

# #白色、灰色
# def white
#   print "\033[",105.to_s, "m","  \033[0m"
# end
# def gray
#   print "\033[", 45.to_s, "m","  \033[0m"
# end

# #白色、灰色
# def white
#   print "\033[",106.to_s, "m","  \033[0m"
# end
# def gray
#   print "\033[", 46.to_s, "m","  \033[0m"
# end

#白色
def white
  print "\033[",107.to_s, "m","  \033[0m"
end
#うすめの灰色
def gray
  print "\033[", 47.to_s, "m","  \033[0m"
end

def space
  print "  "
end

print "\n"
# for b in 40..47
#   s = b.to_s
#   # print "\033[", 40.to_s, "m    ", 41.to_s, "   \033[0m "
#   # \033でESCを表す。ESC [ 色コード m の順番で色付け開始、ESC [ 0 m で色付け終了
#   print "\033[", 107.to_s, "m","  \033[0m"
#   print "\033[", 47.to_s, "m","  \033[0m"
#   print "\n"
# end
black
print "\n"
white;gray;space
gray
print "\n"
# for c in [ 30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97 ]
#   s = c.to_s
#   print "\033[", s, "m ","     \033[0m "
#   for b in 40..47
#     s = c.to_s + ";" + b.to_s
#     print "\033[", s, "m ", s, "   \033[0m "
#   end
#   print "\n"
#   for a in [ 1, 4 ]
#     s = c.to_s + ";" + a.to_s
#     print "\033[", s, "m ", s, " \033[0m "
#     for b in 40..47
#       s = c.to_s + ";" + b.to_s + ";" + a.to_s
#       print "\033[", s, "m ", s, " \033[0m "
#     end
#     print "\n"
#   end
# end

