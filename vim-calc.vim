function Calc()
  "echo getline(".")
  let s:s = getline(".")
  " echo s:s
  silent! let s:result = trim(system("python3 ~/Github/vim-calc/build-up/calc.py " . s:s))
  echo "Result: " . str2nr(s:result)
  "s:result
endfunc
