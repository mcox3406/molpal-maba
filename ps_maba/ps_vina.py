import sys
import os
import ray
import pyscreener as ps

ray.init(num_cpus=16)  

input_file = "data/ligs/liquid_stock_first100k.csv"
output_dir = "data/outputs/full_run_100k"

os.makedirs(output_dir, exist_ok=True)

metadata = ps.build_metadata("vina")
virtual_screen = ps.virtual_screen("vina",
                                  ["data/xtals/5ovk.pdb"],
                                  (0.0, 24.0, 40.0), (20, 22, 25),
                                  metadata, 
                                  ncpu=16) 

supply = ps.LigandSupply([input_file])

print(f"Starting virtual screening with {len(supply.ligands)} ligands")
scores = virtual_screen(supply.ligands)


# write scores to output file
with open(f"{output_dir}/scores.txt", "w") as f:
    for score in scores:
        f.write(f"{score}\n")

virtual_screen.collect_files(output_dir)

print(f"Virtual screening complete. Results saved to {output_dir}")
