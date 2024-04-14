from ascii_magic import AsciiArt

my_art = AsciiArt.from_image("tiger.jpg")
my_art.to_terminal(columns=100,char='#')#adjust columns and char