import sys
import ray
ray.init()

import pyscreener as ps

if len(sys.argv) > 1:
    shard_id = sys.argv[1]
else:
    shard_id = "1"  # default value

shard_path = f"/pool001/mcox340/molpal-maba/ps_maba/data/ligs/shards/liquid_stock_first10k_shard{shard_id}.csv"

metadata = ps.build_metadata("vina")
virtual_screen = ps.virtual_screen("vina",
                                   ["/pool001/mcox340/molpal-maba/ps_maba/data/xtals/5ovk.pdb"],
                                   (3.47112728, 20.33074552, 46.54234543), (30, 30, 30),
                                   metadata, ncpu=8)
supply = ps.LigandSupply([shard_path])
scores = virtual_screen(supply.ligands)

# virtual_screen.collect_files(f'/pool001/mcox340/molpal-maba/ps_maba/data/outputs/shards/{shard_id}')
with open(f'/pool001/mcox340/molpal-maba/ps_maba/data/outputs/shards/{shard_id}/scores.txt', "w") as f:
    for score in scores:
        f.write(f"{score}\n")
