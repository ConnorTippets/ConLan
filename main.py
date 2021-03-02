def compute_code(self, code:str):
        output = []
        if code.__class__.__name__ == 'list':
            pass
        else:
            code = code.split('\n')
        var_dict = {}
        for x in range(len(code)):
            if code[x].startswith('var'):
                format = code[x][4:]
                name, content = format.split(':')
                if content.startswith('"'):
                    var_dict[name] = content.replace('"', '')
                elif content.startswith('%'):
                    try:
                        var_dict[name] = var_dict[content.replace('%', '')]
                    except KeyError:
                        var = content.rstrip('"')
                        return f"NameError: \"{var}\" does not exist"
                else:
                    return f'NameError: Unknown Name "{content.split()[0]}"'
            elif code[x].startswith('echo'):
                if code[x][5:].startswith('%'):
                  try:
                      output.append(var_dict[code[x][5:].split('%')[1]])
                  except KeyError:
                      return f'NameError: "{code[x][5:].split("%")[1]}" does not exist'
                else:
                  if code[x][5:].startswith('"'):
                      if code[x][5:].endswith('"'):
                          output.append(code[x].removeprefix('echo "').removesuffix('"'))
                      else:
                          return "SyntaxError: '\"' not matched"
                  else:
                      return f'NameError: Unknown Name "{code[x][5:].split()[0]}"'
            elif code[x].startswith('newline'):
                output.append('\n')
            else:
                return f'NameError: Unknown Name "{code[x].split()[0]}"'
        return '\n'.join(output)

code = []
while True:
    line = input('>>> ')
    if line == 'run':
        compute_code(code)
        break
    code.append(line)
