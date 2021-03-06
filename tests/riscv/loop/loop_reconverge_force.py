#
# Copyright (C) [2020] Futurewei Technologies, Inc.
#
# FORCE-RISCV is licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR
# FIT FOR A PARTICULAR PURPOSE.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from riscv.EnvRISCV import EnvRISCV
from riscv.GenThreadRISCV import GenThreadRISCV
from LoopTestSequence import LoopTestSequence

## This test verifies that a standard loop will automatically reconverge to the loop control
# instructions when taking a different execution path from the prior iteration.
class MainSequence(LoopTestSequence):

    def __init__(self, gen_thread, name=None):
        super().__init__(gen_thread, name)

        self._mInstructionWeights = {
            'ADDI##RISCV': 10,
            'ADDW##RISCV': 10,
            'BEQ##RISCV': 2,
            'BGE##RISCV': 2,
            'BGEU##RISCV': 2,
            'BLT##RISCV': 2,
            'BLTU##RISCV': 2,
            'BNE##RISCV': 2,
            'LUI##RISCV': 10,
            'SLLI#RV64I#RISCV': 10,
            'SRLI#RV64I#RISCV': 10,
        }

    ## Return a dictionary of names of instructions to generate in the loop body with their
    # corresponding weights.
    def getInstructionWeights(self):
        return self._mInstructionWeights


MainSequenceClass = MainSequence
GenThreadClass = GenThreadRISCV
EnvClass = EnvRISCV

