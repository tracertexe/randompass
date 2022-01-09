import string
from random import sample

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
total = letters + digits + punctuation

print("""

                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     - EDIT BY TRACERTEXE -
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {             ☪☪☪      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`

""")

print("\033[93m************************************")

length = int(input("\033[93m Uzunluk: "))

password = "".join(sample(total, length))

print("************************************")

print("\033[93m Parola:  ",password)

print("************************************")
