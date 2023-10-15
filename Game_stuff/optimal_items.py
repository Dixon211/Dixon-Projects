def optimal(iron = 0, copper =0, limestone=0):
    # part: [(material, amount), (material, amount), output]
    base_materials = {"iron": iron, "copper": copper, "limestone": limestone}
    parts = {
        ["Iron_Rod", 15]: [["iron", 15]],
        ["Iron_Plate",20]: [["iron", 30]],
        ["Wire", 30]:[["copper", 15]],
        ["Copper_Sheet", 10]: [["copper", 20]],
        ["Screw", 40]: [["Iron_Rod", 10]],
        ["Cable", 30]: [["Wire", 60]],
        ["Concrete", 15]: [["limestone", 45]],
        ["Reinforced_Plate", 5]:[["Iron_Plate", 30], ["Screw", 60]],
        ["Modular_Frame", 2]: [["Reinforced_Plate", 3], ["Iron_Rod", 12]],
        ["Rotor", 4]: [["Iron_Rod", 20], ["Screw", 100]]
    }
    for part, materials in parts:
        memory = []
        for material in materials:
            