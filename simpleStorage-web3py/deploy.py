from solcx import  compile_standard
import json

# import solcx
# solcx.install_solc('0.6.0')

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)


compile_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    },
    solc_version="0.6.0"
)


with open("compiled_code.json", "w") as file:
    json.dump(compile_sol, file)