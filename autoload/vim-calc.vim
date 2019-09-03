let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h') . '/calc.py'
function Calc()
  let s = getline(".")
  let calc_str = "python3 " . s:path . " \"" . s . "\""
  let result_str = trim(system(calc_str))
  let result_array = split(result_str, '\')
  let result = ""
  let done = 0
  let i = 0
  while !done
    let result_array[i] = trim(result_array[i])
    let i += 1
    if i >= len(result_array)
      break
    endif
  endwhile
  if result_array[0] == "0"
    echom "Error: " . result_array[1]
  elseif result_array[0] == "1"
    echom result_array[2] . " = " . result_array[1]
  else
    echom "Script Error, contact the developer... or just figure it out!"
  endif
endfunc


