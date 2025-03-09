import ray
ray.init()

import pyscreener as ps

metadata = ps.build_metadata("vina")
virtual_screen = ps.virtual_screen("vina", 
                                   ["/Users/matthewcox/Documents/GitHub/molpal-maba/pyscreener_test/integration-tests/inputs/5WIU.pdb"], 
                                   (-18.2, 14.4, -16.1), (15.4, 13.9, 14.5), 
                                   metadata, ncpu=1)
supply = ps.LigandSupply(['/Users/matthewcox/Documents/GitHub/molpal-maba/pyscreener_test/integration-tests/inputs/ligands_small.csv'])
scores = virtual_screen(supply.ligands)
print(scores)
