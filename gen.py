

import random
import string

provider = """terraform {
  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "3.1.1"
    }
  }
}\n\n"""

resource = """resource "null_resource" "test{0}" {{
  triggers = {{
    a = "{1}"
    b = "{1}"
    c = "{1}"
  }}
}}\n\n"""

def main():
    with open("main.tf", "w") as file:
        file.write(provider)
        for x in range(1000):
            file.write(resource.format(x, ''.join(random.choice(string.ascii_lowercase) for i in range(2000))))

if __name__ == "__main__":
    main()
