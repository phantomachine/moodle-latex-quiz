for x in range(2,10):
          for y in range(2,10):
            if x > y:
              if x/y == x//y:
                points=4
              else:
                points=3
              print(rf"""\begin{{cloze}}[points={points}]{{Arithmetic Quiz {(x,y)}}}
              Solve the following tasks!\\
              \begin{{numerical}}
              ${x} + {y} =$
              \item {x+y}
              \end{{numerical}}\\
              \begin{{numerical}}
              ${x} - {y} =$
              \item {x-y}
              \end{{numerical}}\\
              \begin{{numerical}}
              ${x} \cdot {y} =$
              \item {x*y}
              \end{{numerical}}\\""")
              if x/y == x//y:
                print(rf"""\begin{{numerical}}
                ${x} : {y} =$
                \item {x//y}
                \end{{numerical}}\\""")
              print(rf"\end{{cloze}}")
    
