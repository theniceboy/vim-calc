function Calc()
  "let s = substitute(getline("."), ' ', '', 'g')
  let s = getline(".")
  let calc_str = "python3 ~/Github/vim-calc/build-up/calc.py \"" . s . "\""
  let result = trim(system(calc_str))
  echo result
endfunc
