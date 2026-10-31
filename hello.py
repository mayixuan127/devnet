# Hello World exercise for Solana Playground (Seahorse).
# Playground fills in the program ID when you build.
from seahorse.prelude import *

declare_id('')

@instruction
def hello(signer: Signer):
    print('Hello, World!')
