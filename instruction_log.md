|      | Opcode   | Instruction           | Translation                |
|-----:|:---------|:----------------------|:---------------------------|
|    0 | add      | add	x0, x0, :lo12:ts                       | add	x10, x10, %lo(ts)               |
|    1 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|    2 | add      | add	x0, x1, x0                       | add	x10, x11, x10               |
|    3 | add      | add	sp, sp, x16                       | add	x2, x2, x27               |
|    4 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|    5 | add      | add	sp, sp, x16                       | add	x2, x2, x27               |
|    6 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|    7 | add      | add	w1, w0, 1                       | addiw	x11, x10, 1               |
|    8 | add      | add	x0, x0, :lo12:.LC1                       | add	x10, x10, %lo(.LC1)               |
|    9 | add      | add	x0, x0, :lo12:.LC4                       | add	x10, x10, %lo(.LC4)               |
|   10 | add      | add	x0, x0, :lo12:non_atomic_counter                       | add	x10, x10, %lo(non_atomic_counter)               |
|   11 | add      | add	x0, x0, :lo12:.LC0                       | add	x10, x10, %lo(.LC0)               |
|   12 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|   13 | add      | add	x0, x0, :lo12:atomic_counter                       | add	x10, x10, %lo(atomic_counter)               |
|   14 | add      | add	x0, x0, :lo12:.LC0                       | add	x10, x10, %lo(.LC0)               |
|   15 | add      | add	x0, x0, :lo12:atomic_counter                       | add	x10, x10, %lo(atomic_counter)               |
|   16 | add      | add	w1, w1, w0                       | addw	x11, x11, x10               |
|   17 | add      | add	x0, x0, :lo12:.LC3                       | add	x10, x10, %lo(.LC3)               |
|   18 | add      | add	x0, x1, x0                       | add	x10, x11, x10               |
|   19 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|   20 | add      | add	x0, x0, :lo12:.LC0                       | add	x10, x10, %lo(.LC0)               |
|   21 | add      | add	x0, x0, :lo12:.LC1                       | add	x10, x10, %lo(.LC1)               |
|   22 | add      | add	x0, x0, :lo12:.LC1                       | add	x10, x10, %lo(.LC1)               |
|   23 | add      | add	w0, w1, w0                       | addw	x10, x11, x10               |
|   24 | add      | add	w1, w0, 1                       | addiw	x11, x10, 1               |
|   25 | add      | add	x0, x0, :lo12:.LC2                       | add	x10, x10, %lo(.LC2)               |
|   26 | add      | add	x0, x0, :lo12:non_atomic_counter                       | add	x10, x10, %lo(non_atomic_counter)               |
|   27 | add      | add	x0, x0, :lo12:.LC14                       | add	x10, x10, %lo(.LC14)               |
|   28 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|   29 | add      | add	x0, x0, :lo12:.LC9                       | add	x10, x10, %lo(.LC9)               |
|   30 | add      | add	w1, w1, w0                       | addw	x11, x11, x10               |
|   31 | add      | add	x0, x0, :lo12:.LC1                       | add	x10, x10, %lo(.LC1)               |
|   32 | add      | add	x0, x0, :lo12:xor_check                       | add	x10, x10, %lo(xor_check)               |
|   33 | add      | add	x0, x0, :lo12:.LC0                       | add	x10, x10, %lo(.LC0)               |
|   34 | add      | add	x0, x0, :lo12:.LC2                       | add	x10, x10, %lo(.LC2)               |
|   35 | add      | add	x0, x0, :lo12:or_check                       | add	x10, x10, %lo(or_check)               |
|   36 | add      | add	x0, x0, :lo12:.LC3                       | add	x10, x10, %lo(.LC3)               |
|   37 | add      | add	x0, x0, :lo12:and_check                       | add	x10, x10, %lo(and_check)               |
|   38 | add      | add	x1, x29, 32                       | addi	x11, x8, 32               |
|   39 | add      | add	x0, x0, :lo12:.LC4                       | add	x10, x10, %lo(.LC4)               |
|   40 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|   41 | add      | add	x0, x0, :lo12:and_check_2                       | add	x10, x10, %lo(and_check_2)               |
|   42 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|   43 | add      | add	x0, x0, :lo12:.LC7                       | add	x10, x10, %lo(.LC7)               |
|   44 | add      | add	x0, x0, :lo12:min_check                       | add	x10, x10, %lo(min_check)               |
|   45 | add      | add	x0, x0, :lo12:.LC6                       | add	x10, x10, %lo(.LC6)               |
|   46 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|   47 | add      | add	x0, x0, :lo12:max_check                       | add	x10, x10, %lo(max_check)               |
|   48 | add      | add	x0, x0, :lo12:.LC7                       | add	x10, x10, %lo(.LC7)               |
|   49 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|   50 | add      | add	x0, x0, :lo12:unsigned_min_check                       | add	x10, x10, %lo(unsigned_min_check)               |
|   51 | add      | add	x0, x0, :lo12:.LC1                       | add	x10, x10, %lo(.LC1)               |
|   52 | add      | add	x0, x0, :lo12:.LC8                       | add	x10, x10, %lo(.LC8)               |
|   53 | add      | add	x0, x1, x0                       | add	x10, x11, x10               |
|   54 | add      | add	x0, x0, :lo12:unsigned_max_check                       | add	x10, x10, %lo(unsigned_max_check)               |
|   55 | add      | add	x0, x0, :lo12:.LC5                       | add	x10, x10, %lo(.LC5)               |
|   56 | add      | add	x0, x0, :lo12:.LC5                       | add	x10, x10, %lo(.LC5)               |
|   57 | add      | add	x0, x0, :lo12:total_sum                       | add	x10, x10, %lo(total_sum)               |
|   58 | add      | add	x0, x0, :lo12:.LC3                       | add	x10, x10, %lo(.LC3)               |
|   59 | add      | add	x0, x0, :lo12:.LC2                       | add	x10, x10, %lo(.LC2)               |
|   60 | add      | add	x0, x0, :lo12:.LC15                       | add	x10, x10, %lo(.LC15)               |
|   61 | add      | add	x0, x0, :lo12:.LC9                       | add	x10, x10, %lo(.LC9)               |
|   62 | add      | add	x0, x0, 15                       | addi	x10, x10, 15               |
|   63 | add      | add	x0, x0, 3                       | addi	x10, x10, 3               |
|   64 | add      | add	x0, x0, :lo12:.LC3                       | add	x10, x10, %lo(.LC3)               |
|   65 | add      | add	x0, x0, :lo12:.LC4                       | add	x10, x10, %lo(.LC4)               |
|   66 | add      | add	x0, x0, :lo12:.LC4                       | add	x10, x10, %lo(.LC4)               |
|   67 | add      | add	x0, x0, :lo12:.LC10                       | add	x10, x10, %lo(.LC10)               |
|   68 | add      | add	x0, x0, :lo12:.LC5                       | add	x10, x10, %lo(.LC5)               |
|   69 | add      | add	x1, x29, 40                       | addi	x11, x8, 40               |
|   70 | add      | add	x0, x0, :lo12:.LC16                       | add	x10, x10, %lo(.LC16)               |
|   71 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|   72 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|   73 | add      | add	x4, x1, x0                       | add	x14, x11, x10               |
|   74 | add      | add	x0, x0, :lo12:.LC0                       | add	x10, x10, %lo(.LC0)               |
|   75 | add      | add	x0, x0, :lo12:.LC11                       | add	x10, x10, %lo(.LC11)               |
|   76 | add      | add	w1, w1, w0                       | addw	x11, x11, x10               |
|   77 | add      | add	x0, x0, :lo12:.LC3                       | add	x10, x10, %lo(.LC3)               |
|   78 | add      | add	x0, x0, :lo12:mythread                       | add	x10, x10, %lo(mythread)               |
|   79 | add      | add	x0, x0, :lo12:.LC12                       | add	x10, x10, %lo(.LC12)               |
|   80 | add      | add	x0, x0, :lo12:.LC1                       | add	x10, x10, %lo(.LC1)               |
|   81 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|   82 | add      | add	x0, x0, :lo12:.LC0                       | add	x10, x10, %lo(.LC0)               |
|   83 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|   84 | add      | add	x0, x0, :lo12:.LC13                       | add	x10, x10, %lo(.LC13)               |
|   85 | add      | add	x0, x0, :lo12:.LC2                       | add	x10, x10, %lo(.LC2)               |
|   86 | add      | add	x0, x0, 3                       | addi	x10, x10, 3               |
|   87 | add      | add	x0, x0, :lo12:.LC5                       | add	x10, x10, %lo(.LC5)               |
|   88 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|   89 | add      | add	x0, x0, :lo12:.LC2                       | add	x10, x10, %lo(.LC2)               |
|   90 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|   91 | add      | add	x0, x0, :lo12:.LC4                       | add	x10, x10, %lo(.LC4)               |
|   92 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|   93 | add      | add	x0, x0, :lo12:.LC3                       | add	x10, x10, %lo(.LC3)               |
|   94 | add      | add	x0, x1, x0                       | add	x10, x11, x10               |
|   95 | add      | add	w0, w1, w0                       | addw	x10, x11, x10               |
|   96 | add      | add	x0, x0, :lo12:.LC1                       | add	x10, x10, %lo(.LC1)               |
|   97 | add      | add	x0, x0, :lo12:.LC5                       | add	x10, x10, %lo(.LC5)               |
|   98 | add      | add	w1, w1, w0                       | addw	x11, x11, x10               |
|   99 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  100 | add      | add	x0, x0, :lo12:.LC6                       | add	x10, x10, %lo(.LC6)               |
|  101 | add      | add	x0, x0, :lo12:.LC18                       | add	x10, x10, %lo(.LC18)               |
|  102 | add      | add	x0, x0, :lo12:.LC4                       | add	x10, x10, %lo(.LC4)               |
|  103 | add      | add	x0, x0, :lo12:.LC6                       | add	x10, x10, %lo(.LC6)               |
|  104 | add      | add	x0, x0, 15                       | addi	x10, x10, 15               |
|  105 | add      | add	x0, x0, 3                       | addi	x10, x10, 3               |
|  106 | add      | add	x0, x0, :lo12:.LC7                       | add	x10, x10, %lo(.LC7)               |
|  107 | add      | add	x0, x0, :lo12:.LC5                       | add	x10, x10, %lo(.LC5)               |
|  108 | add      | add	x1, x1, x0                       | add	x11, x11, x10               |
|  109 | add      | add	x0, x0, :lo12:.LC17                       | add	x10, x10, %lo(.LC17)               |
|  110 | add      | add	x0, x0, :lo12:.LC6                       | add	x10, x10, %lo(.LC6)               |
|  111 | add      | add	w1, w1, w0                       | addw	x11, x11, x10               |
|  112 | add      | add	x1, x29, 40                       | addi	x11, x8, 40               |
|  113 | add      | add	x0, x0, :lo12:.LC1                       | add	x10, x10, %lo(.LC1)               |
|  114 | add      | add	x0, x0, :lo12:.LC8                       | add	x10, x10, %lo(.LC8)               |
|  115 | add      | add	x0, x0, 3                       | addi	x10, x10, 3               |
|  116 | add      | add	x0, x1, x0                       | add	x10, x11, x10               |
|  117 | add      | add	x0, x0, :lo12:.LC2                       | add	x10, x10, %lo(.LC2)               |
|  118 | add      | add	x4, x1, x0                       | add	x14, x11, x10               |
|  119 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|  120 | add      | add	sp, sp, x16                       | add	x2, x2, x27               |
|  121 | add      | add	sp, x29, 0                       | addi	x2, x8, 0               |
|  122 | add      | add	x0, x0, :lo12:and_check                       | add	x10, x10, %lo(and_check)               |
|  123 | add      | add	x0, x0, :lo12:current_thread_index                       | add	x10, x10, %lo(current_thread_index)               |
|  124 | add      | add	x0, x0, :lo12:.LC10                       | add	x10, x10, %lo(.LC10)               |
|  125 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|  126 | add      | add	x0, x0, :lo12:.LC1                       | add	x10, x10, %lo(.LC1)               |
|  127 | add      | add	x0, x0, :lo12:.LC4                       | add	x10, x10, %lo(.LC4)               |
|  128 | add      | add	x0, x0, :lo12:.LC2                       | add	x10, x10, %lo(.LC2)               |
|  129 | add      | add	x1, x29, 40                       | addi	x11, x8, 40               |
|  130 | add      | add	sp, sp, x16                       | add	x2, x2, x27               |
|  131 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|  132 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  133 | add      | add	x0, x1, x0                       | add	x10, x11, x10               |
|  134 | add      | add	x0, x0, :lo12:or_check                       | add	x10, x10, %lo(or_check)               |
|  135 | add      | add	x0, x0, :lo12:mythread                       | add	x10, x10, %lo(mythread)               |
|  136 | add      | add	x0, x29, 32                       | addi	x10, x8, 32               |
|  137 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  138 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|  139 | add      | add	x0, x29, 24                       | addi	x10, x8, 24               |
|  140 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|  141 | add      | add	x0, x0, :lo12:.LC5                       | add	x10, x10, %lo(.LC5)               |
|  142 | add      | add	x0, x0, :lo12:max_check                       | add	x10, x10, %lo(max_check)               |
|  143 | add      | add	x0, x0, :lo12:unsigned_min_check                       | add	x10, x10, %lo(unsigned_min_check)               |
|  144 | add      | add	x0, x29, 24                       | addi	x10, x8, 24               |
|  145 | add      | add	x0, x0, :lo12:current_thread_index                       | add	x10, x10, %lo(current_thread_index)               |
|  146 | add      | add	x0, x0, :lo12:unsigned_max_check                       | add	x10, x10, %lo(unsigned_max_check)               |
|  147 | add      | add	x0, x0, :lo12:.LC8                       | add	x10, x10, %lo(.LC8)               |
|  148 | add      | add	x0, x0, :lo12:.LC9                       | add	x10, x10, %lo(.LC9)               |
|  149 | add      | add	x0, x0, :lo12:min_check                       | add	x10, x10, %lo(min_check)               |
|  150 | add      | add	w0, w0, w1                       | addw	x10, x10, x11               |
|  151 | add      | add	x0, x0, :lo12:.LC3                       | add	x10, x10, %lo(.LC3)               |
|  152 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  153 | add      | add	x0, x0, :lo12:.LC0                       | add	x10, x10, %lo(.LC0)               |
|  154 | add      | add	w0, w1, w0                       | addw	x10, x11, x10               |
|  155 | add      | add	x0, x0, :lo12:.LC13                       | add	x10, x10, %lo(.LC13)               |
|  156 | add      | add	sp, sp, 32                       | addi	x2, x2, 32               |
|  157 | add      | add	x0, x29, 24                       | addi	x10, x8, 24               |
|  158 | add      | add	x2, x29, 32768                       | li	s10, 32768                  |
|      |          |                       | add	x12, x8, s10               |
|  159 | add      | add	sp, sp, 16                       | addi	x2, x2, 16               |
|  160 | add      | add	x0, x0, :lo12:and_check_2                       | add	x10, x10, %lo(and_check_2)               |
|  161 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|  162 | add      | add	x0, x0, :lo12:.LC2                       | add	x10, x10, %lo(.LC2)               |
|  163 | add      | add	x0, x0, :lo12:xor_check                       | add	x10, x10, %lo(xor_check)               |
|  164 | add      | add	x1, x1, x0                       | add	x11, x11, x10               |
|  165 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  166 | add      | add	x0, x0, :lo12:.LC1                       | add	x10, x10, %lo(.LC1)               |
|  167 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  168 | add      | add	x1, x29, 40                       | addi	x11, x8, 40               |
|  169 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  170 | add      | add	x29, sp, 0                       | addi	x8, x2, 0               |
|  171 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  172 | add      | add	x0, x0, :lo12:.LC19                       | add	x10, x10, %lo(.LC19)               |
|  173 | add      | add	x0, x0, :lo12:non_atomic_counter                       | add	x10, x10, %lo(non_atomic_counter)               |
|  174 | add      | add	w0, w1, w0                       | addw	x10, x11, x10               |
|  175 | add      | add	x0, x1, x0                       | add	x10, x11, x10               |
|  176 | add      | add	x1, x29, 32768                       | li	s10, 32768                  |
|      |          |                       | add	x11, x8, s10               |
|  177 | add      | add	x1, x29, 24                       | addi	x11, x8, 24               |
|  178 | add      | add	x0, x0, :lo12:total_sum                       | add	x10, x10, %lo(total_sum)               |
|  179 | add      | add	x0, x0, :lo12:atomic_counter                       | add	x10, x10, %lo(atomic_counter)               |
|  180 | add      | add	x0, x0, :lo12:.LC0                       | add	x10, x10, %lo(.LC0)               |
|  181 | add      | add	x0, x0, :lo12:.LC11                       | add	x10, x10, %lo(.LC11)               |
|  182 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  183 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  184 | add      | add	x0, x0, :lo12:atomic_counter                       | add	x10, x10, %lo(atomic_counter)               |
|  185 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  186 | add      | add	w0, w0, 1                       | addiw	x10, x10, 1               |
|  187 | add      | add	x0, x0, :lo12:.LC12                       | add	x10, x10, %lo(.LC12)               |
|  188 | add      | add	x0, x0, :lo12:.LC0                       | add	x10, x10, %lo(.LC0)               |
|  189 | add      | add	x1, x29, 32                       | addi	x11, x8, 32               |
|  190 | add      | add	x0, x0, :lo12:.LC2                       | add	x10, x10, %lo(.LC2)               |
|  191 | adrp     | adrp	x0, .LC12                       | lui	x10, %hi(.LC12)               |
|  192 | adrp     | adrp	x0, .LC3                       | lui	x10, %hi(.LC3)               |
|  193 | adrp     | adrp	x0, .LC5                       | lui	x10, %hi(.LC5)               |
|  194 | adrp     | adrp	x0, .LC2                       | lui	x10, %hi(.LC2)               |
|  195 | adrp     | adrp	x0, .LC5                       | lui	x10, %hi(.LC5)               |
|  196 | adrp     | adrp	x0, .LC7                       | lui	x10, %hi(.LC7)               |
|  197 | adrp     | adrp	x0, .LC6                       | lui	x10, %hi(.LC6)               |
|  198 | adrp     | adrp	x0, ts                       | lui	x10, %hi(ts)               |
|  199 | adrp     | adrp	x0, min_check                       | lui	x10, %hi(min_check)               |
|  200 | adrp     | adrp	x0, .LC2                       | lui	x10, %hi(.LC2)               |
|  201 | adrp     | adrp	x0, .LC9                       | lui	x10, %hi(.LC9)               |
|  202 | adrp     | adrp	x0, .LC0                       | lui	x10, %hi(.LC0)               |
|  203 | adrp     | adrp	x0, max_check                       | lui	x10, %hi(max_check)               |
|  204 | adrp     | adrp	x0, .LC6                       | lui	x10, %hi(.LC6)               |
|  205 | adrp     | adrp	x0, .LC12                       | lui	x10, %hi(.LC12)               |
|  206 | adrp     | adrp	x0, .LC13                       | lui	x10, %hi(.LC13)               |
|  207 | adrp     | adrp	x0, .LC4                       | lui	x10, %hi(.LC4)               |
|  208 | adrp     | adrp	x0, :got:__stack_chk_guard                       | lui	x10, %hi(__stack_chk_guard)               |
|  209 | adrp     | adrp	x0, current_thread_index                       | lui	x10, %hi(current_thread_index)               |
|  210 | adrp     | adrp	x0, .LC1                       | lui	x10, %hi(.LC1)               |
|  211 | adrp     | adrp	x0, .LC1                       | lui	x10, %hi(.LC1)               |
|  212 | adrp     | adrp	x0, .LC0                       | lui	x10, %hi(.LC0)               |
|  213 | adrp     | adrp	x0, .LC4                       | lui	x10, %hi(.LC4)               |
|  214 | adrp     | adrp	x0, .LC4                       | lui	x10, %hi(.LC4)               |
|  215 | adrp     | adrp	x0, .LC11                       | lui	x10, %hi(.LC11)               |
|  216 | adrp     | adrp	x0, .LC10                       | lui	x10, %hi(.LC10)               |
|  217 | adrp     | adrp	x0, xor_check                       | lui	x10, %hi(xor_check)               |
|  218 | adrp     | adrp	x0, .LC3                       | lui	x10, %hi(.LC3)               |
|  219 | adrp     | adrp	x0, or_check                       | lui	x10, %hi(or_check)               |
|  220 | adrp     | adrp	x0, .LC9                       | lui	x10, %hi(.LC9)               |
|  221 | adrp     | adrp	x0, .LC1                       | lui	x10, %hi(.LC1)               |
|  222 | adrp     | adrp	x0, total_sum                       | lui	x10, %hi(total_sum)               |
|  223 | adrp     | adrp	x0, .LC16                       | lui	x10, %hi(.LC16)               |
|  224 | adrp     | adrp	x0, :got:__stack_chk_guard                       | lui	x10, %hi(__stack_chk_guard)               |
|  225 | adrp     | adrp	x0, .LC2                       | lui	x10, %hi(.LC2)               |
|  226 | adrp     | adrp	x0, :got:__stack_chk_guard                       | lui	x10, %hi(__stack_chk_guard)               |
|  227 | adrp     | adrp	x0, .LC15                       | lui	x10, %hi(.LC15)               |
|  228 | adrp     | adrp	x0, .LC5                       | lui	x10, %hi(.LC5)               |
|  229 | adrp     | adrp	x0, .LC0                       | lui	x10, %hi(.LC0)               |
|  230 | adrp     | adrp	x0, and_check                       | lui	x10, %hi(and_check)               |
|  231 | adrp     | adrp	x0, mythread                       | lui	x10, %hi(mythread)               |
|  232 | adrp     | adrp	x0, .LC8                       | lui	x10, %hi(.LC8)               |
|  233 | adrp     | adrp	x0, .LC10                       | lui	x10, %hi(.LC10)               |
|  234 | adrp     | adrp	x0, .LC11                       | lui	x10, %hi(.LC11)               |
|  235 | adrp     | adrp	x0, atomic_counter                       | lui	x10, %hi(atomic_counter)               |
|  236 | adrp     | adrp	x0, and_check_2                       | lui	x10, %hi(and_check_2)               |
|  237 | adrp     | adrp	x0, .LC6                       | lui	x10, %hi(.LC6)               |
|  238 | adrp     | adrp	x0, .LC17                       | lui	x10, %hi(.LC17)               |
|  239 | adrp     | adrp	x0, .LC0                       | lui	x10, %hi(.LC0)               |
|  240 | adrp     | adrp	x0, .LC1                       | lui	x10, %hi(.LC1)               |
|  241 | adrp     | adrp	x0, .LC18                       | lui	x10, %hi(.LC18)               |
|  242 | adrp     | adrp	x0, .LC14                       | lui	x10, %hi(.LC14)               |
|  243 | adrp     | adrp	x0, .LC1                       | lui	x10, %hi(.LC1)               |
|  244 | adrp     | adrp	x0, .LC5                       | lui	x10, %hi(.LC5)               |
|  245 | adrp     | adrp	x0, .LC9                       | lui	x10, %hi(.LC9)               |
|  246 | adrp     | adrp	x0, unsigned_max_check                       | lui	x10, %hi(unsigned_max_check)               |
|  247 | adrp     | adrp	x0, .LC3                       | lui	x10, %hi(.LC3)               |
|  248 | adrp     | adrp	x0, .LC8                       | lui	x10, %hi(.LC8)               |
|  249 | adrp     | adrp	x0, unsigned_min_check                       | lui	x10, %hi(unsigned_min_check)               |
|  250 | adrp     | adrp	x0, .LC2                       | lui	x10, %hi(.LC2)               |
|  251 | adrp     | adrp	x0, .LC7                       | lui	x10, %hi(.LC7)               |
|  252 | adrp     | adrp	x0, non_atomic_counter                       | lui	x10, %hi(non_atomic_counter)               |
|  253 | adrp     | adrp	x0, max_check                       | lui	x10, %hi(max_check)               |
|  254 | adrp     | adrp	x0, .LC6                       | lui	x10, %hi(.LC6)               |
|  255 | adrp     | adrp	x0, .LC7                       | lui	x10, %hi(.LC7)               |
|  256 | adrp     | adrp	x0, min_check                       | lui	x10, %hi(min_check)               |
|  257 | adrp     | adrp	x0, .LC5                       | lui	x10, %hi(.LC5)               |
|  258 | adrp     | adrp	x0, .LC2                       | lui	x10, %hi(.LC2)               |
|  259 | adrp     | adrp	x0, total_sum                       | lui	x10, %hi(total_sum)               |
|  260 | adrp     | adrp	x0, .LC1                       | lui	x10, %hi(.LC1)               |
|  261 | adrp     | adrp	x0, .LC1                       | lui	x10, %hi(.LC1)               |
|  262 | adrp     | adrp	x0, atomic_counter                       | lui	x10, %hi(atomic_counter)               |
|  263 | adrp     | adrp	x0, .LC0                       | lui	x10, %hi(.LC0)               |
|  264 | adrp     | adrp	x0, xor_check                       | lui	x10, %hi(xor_check)               |
|  265 | adrp     | adrp	x0, mythread                       | lui	x10, %hi(mythread)               |
|  266 | adrp     | adrp	x0, .LC2                       | lui	x10, %hi(.LC2)               |
|  267 | adrp     | adrp	x0, .LC19                       | lui	x10, %hi(.LC19)               |
|  268 | adrp     | adrp	x0, .LC3                       | lui	x10, %hi(.LC3)               |
|  269 | adrp     | adrp	x0, and_check                       | lui	x10, %hi(and_check)               |
|  270 | adrp     | adrp	x0, .LC4                       | lui	x10, %hi(.LC4)               |
|  271 | adrp     | adrp	x0, .LC0                       | lui	x10, %hi(.LC0)               |
|  272 | adrp     | adrp	x0, and_check_2                       | lui	x10, %hi(and_check_2)               |
|  273 | adrp     | adrp	x0, or_check                       | lui	x10, %hi(or_check)               |
|  274 | adrp     | adrp	x1, :got:__stack_chk_guard                       | lui	x11, %hi(__stack_chk_guard)               |
|  275 | adrp     | adrp	x1, :got:__stack_chk_guard                       | lui	x11, %hi(__stack_chk_guard)               |
|  276 | adrp     | adrp	x0, non_atomic_counter                       | lui	x10, %hi(non_atomic_counter)               |
|  277 | adrp     | adrp	x0, .LC2                       | lui	x10, %hi(.LC2)               |
|  278 | adrp     | adrp	x0, .LC3                       | lui	x10, %hi(.LC3)               |
|  279 | adrp     | adrp	x0, .LC8                       | lui	x10, %hi(.LC8)               |
|  280 | adrp     | adrp	x0, .LC13                       | lui	x10, %hi(.LC13)               |
|  281 | adrp     | adrp	x0, .LC2                       | lui	x10, %hi(.LC2)               |
|  282 | adrp     | adrp	x0, .LC1                       | lui	x10, %hi(.LC1)               |
|  283 | adrp     | adrp	x0, .LC3                       | lui	x10, %hi(.LC3)               |
|  284 | adrp     | adrp	x0, .LC4                       | lui	x10, %hi(.LC4)               |
|  285 | adrp     | adrp	x0, .LC0                       | lui	x10, %hi(.LC0)               |
|  286 | adrp     | adrp	x0, .LC4                       | lui	x10, %hi(.LC4)               |
|  287 | adrp     | adrp	x0, atomic_counter                       | lui	x10, %hi(atomic_counter)               |
|  288 | adrp     | adrp	x0, .LC1                       | lui	x10, %hi(.LC1)               |
|  289 | adrp     | adrp	x0, :got:__stack_chk_guard                       | lui	x10, %hi(__stack_chk_guard)               |
|  290 | adrp     | adrp	x1, :got:__stack_chk_guard                       | lui	x11, %hi(__stack_chk_guard)               |
|  291 | adrp     | adrp	x0, .LC5                       | lui	x10, %hi(.LC5)               |
|  292 | adrp     | adrp	x0, unsigned_max_check                       | lui	x10, %hi(unsigned_max_check)               |
|  293 | adrp     | adrp	x0, .LC5                       | lui	x10, %hi(.LC5)               |
|  294 | adrp     | adrp	x0, :got:__stack_chk_guard                       | lui	x10, %hi(__stack_chk_guard)               |
|  295 | adrp     | adrp	x0, :got:__stack_chk_guard                       | lui	x10, %hi(__stack_chk_guard)               |
|  296 | adrp     | adrp	x0, non_atomic_counter                       | lui	x10, %hi(non_atomic_counter)               |
|  297 | adrp     | adrp	x0, .LC0                       | lui	x10, %hi(.LC0)               |
|  298 | adrp     | adrp	x0, current_thread_index                       | lui	x10, %hi(current_thread_index)               |
|  299 | adrp     | adrp	x0, .LC1                       | lui	x10, %hi(.LC1)               |
|  300 | adrp     | adrp	x0, unsigned_min_check                       | lui	x10, %hi(unsigned_min_check)               |
|  301 | adrp     | adrp	x0, .LC3                       | lui	x10, %hi(.LC3)               |
|  302 | adrp     | adrp	x0, .LC0                       | lui	x10, %hi(.LC0)               |
|  303 | adrp     | adrp	x0, atomic_counter                       | lui	x10, %hi(atomic_counter)               |
|  304 | adrp     | adrp	x1, :got:__stack_chk_guard                       | lui	x11, %hi(__stack_chk_guard)               |
|  305 | adrp     | adrp	x0, .LC4                       | lui	x10, %hi(.LC4)               |
|  306 | adrp     | adrp	x0, .LC2                       | lui	x10, %hi(.LC2)               |
|  307 | asr      | asr	w0, w0, 1                       | sraiw	x10, x10, 1               |
|  308 | b        | b	.L11                       | j	.L11               |
|  309 | b        | b	.L2                       | j	.L2               |
|  310 | b        | b	.L9                       | j	.L9               |
|  311 | b        | b	.L6                       | j	.L6               |
|  312 | b        | b	.L4                       | j	.L4               |
|  313 | b        | b	.L13                       | j	.L13               |
|  314 | b        | b	.L3                       | j	.L3               |
|  315 | b        | b	.L2                       | j	.L2               |
|  316 | b        | b	.L13                       | j	.L13               |
|  317 | b        | b	.L8                       | j	.L8               |
|  318 | b        | b	.L6                       | j	.L6               |
|  319 | b        | b	.L23                       | j	.L23               |
|  320 | b        | b	.L4                       | j	.L4               |
|  321 | b        | b	.L20                       | j	.L20               |
|  322 | b        | b	.L6                       | j	.L6               |
|  323 | b        | b	.L2                       | j	.L2               |
|  324 | b        | b	.L15                       | j	.L15               |
|  325 | b        | b	.L8                       | j	.L8               |
|  326 | beq      | beq	.L11                       | beq	x25, x0, .L11               |
|  327 | beq      | beq	.L6                       | beq	x25, x0, .L6               |
|  328 | beq      | beq	.L15                       | beq	x25, x0, .L15               |
|  329 | beq      | beq	.L10                       | beq	x25, x0, .L10               |
|  330 | beq      | beq	.L18                       | beq	x25, x0, .L18               |
|  331 | beq      | beq	.L26                       | beq	x25, x0, .L26               |
|  332 | bge      | bge	.L18                       | bge	x25, x0, .L18               |
|  333 | bge      | bge	.L11                       | bge	x25, x0, .L11               |
|  334 | bgt      | bgt	.L7                       | bgt	x25, x0, .L7               |
|  335 | bl       | bl	printArray                       | call	printArray               |
|  336 | bl       | bl	puts                       | call	puts               |
|  337 | bl       | bl	release_lock                       | call	release_lock               |
|  338 | bl       | bl	__stack_chk_fail                       | call	__stack_chk_fail               |
|  339 | bl       | bl	puts                       | call	puts               |
|  340 | bl       | bl	printf                       | call	printf               |
|  341 | bl       | bl	printArray                       | call	printArray               |
|  342 | bl       | bl	printf                       | call	printf               |
|  343 | bl       | bl	printf                       | call	printf               |
|  344 | bl       | bl	puts                       | call	puts               |
|  345 | bl       | bl	puts                       | call	puts               |
|  346 | bl       | bl	puts                       | call	puts               |
|  347 | bl       | bl	printf                       | call	printf               |
|  348 | bl       | bl	printf                       | call	printf               |
|  349 | bl       | bl	printf                       | call	printf               |
|  350 | bl       | bl	mergeSort                       | call	mergeSort               |
|  351 | bl       | bl	printf                       | call	printf               |
|  352 | bl       | bl	printf                       | call	printf               |
|  353 | bl       | bl	printf                       | call	printf               |
|  354 | bl       | bl	printf                       | call	printf               |
|  355 | bl       | bl	printf                       | call	printf               |
|  356 | bl       | bl	pthread_join                       | call	pthread_join               |
|  357 | bl       | bl	merge                       | call	merge               |
|  358 | bl       | bl	printf                       | call	printf               |
|  359 | bl       | bl	puts                       | call	puts               |
|  360 | bl       | bl	printf                       | call	printf               |
|  361 | bl       | bl	mergeSort                       | call	mergeSort               |
|  362 | bl       | bl	printf                       | call	printf               |
|  363 | bl       | bl	printf                       | call	printf               |
|  364 | bl       | bl	puts                       | call	puts               |
|  365 | bl       | bl	malloc                       | call	malloc               |
|  366 | bl       | bl	printf                       | call	printf               |
|  367 | bl       | bl	putchar                       | call	putchar               |
|  368 | bl       | bl	printf                       | call	printf               |
|  369 | bl       | bl	printf                       | call	printf               |
|  370 | bl       | bl	__stack_chk_fail                       | call	__stack_chk_fail               |
|  371 | bl       | bl	printf                       | call	printf               |
|  372 | bl       | bl	memset                       | call	memset               |
|  373 | bl       | bl	pthread_create                       | call	pthread_create               |
|  374 | bl       | bl	acquire_lock                       | call	acquire_lock               |
|  375 | bl       | bl	printf                       | call	printf               |
|  376 | bl       | bl	printf                       | call	printf               |
|  377 | bl       | bl	printf                       | call	printf               |
|  378 | bl       | bl	__stack_chk_fail                       | call	__stack_chk_fail               |
|  379 | bl       | bl	pthread_join                       | call	pthread_join               |
|  380 | bl       | bl	printf                       | call	printf               |
|  381 | bl       | bl	printf                       | call	printf               |
|  382 | bl       | bl	__stack_chk_fail                       | call	__stack_chk_fail               |
|  383 | bl       | bl	printf                       | call	printf               |
|  384 | bl       | bl	printf                       | call	printf               |
|  385 | bl       | bl	printf                       | call	printf               |
|  386 | bl       | bl	printf                       | call	printf               |
|  387 | bl       | bl	printf                       | call	printf               |
|  388 | bl       | bl	puts                       | call	puts               |
|  389 | bl       | bl	printf                       | call	printf               |
|  390 | bl       | bl	printf                       | call	printf               |
|  391 | bl       | bl	printf                       | call	printf               |
|  392 | bl       | bl	printf                       | call	printf               |
|  393 | bl       | bl	printf                       | call	printf               |
|  394 | bl       | bl	printf                       | call	printf               |
|  395 | bl       | bl	printf                       | call	printf               |
|  396 | bl       | bl	printf                       | call	printf               |
|  397 | bl       | bl	printf                       | call	printf               |
|  398 | bl       | bl	printf                       | call	printf               |
|  399 | bl       | bl	printf                       | call	printf               |
|  400 | bl       | bl	printf                       | call	printf               |
|  401 | bl       | bl	printf                       | call	printf               |
|  402 | bl       | bl	printf                       | call	printf               |
|  403 | bl       | bl	printf                       | call	printf               |
|  404 | bl       | bl	printf                       | call	printf               |
|  405 | bl       | bl	printf                       | call	printf               |
|  406 | bl       | bl	printf                       | call	printf               |
|  407 | bl       | bl	printf                       | call	printf               |
|  408 | bl       | bl	putchar                       | call	putchar               |
|  409 | bl       | bl	printf                       | call	printf               |
|  410 | bl       | bl	malloc                       | call	malloc               |
|  411 | bl       | bl	printf                       | call	printf               |
|  412 | bl       | bl	printf                       | call	printf               |
|  413 | bl       | bl	printf                       | call	printf               |
|  414 | bl       | bl	printf                       | call	printf               |
|  415 | bl       | bl	puts                       | call	puts               |
|  416 | bl       | bl	nanosleep                       | call	nanosleep               |
|  417 | bl       | bl	printf                       | call	printf               |
|  418 | bl       | bl	printf                       | call	printf               |
|  419 | bl       | bl	printf                       | call	printf               |
|  420 | bl       | bl	printf                       | call	printf               |
|  421 | bl       | bl	__stack_chk_fail                       | call	__stack_chk_fail               |
|  422 | bl       | bl	pthread_create                       | call	pthread_create               |
|  423 | bl       | bl	puts                       | call	puts               |
|  424 | bl       | bl	srand                       | call	srand               |
|  425 | bl       | bl	printf                       | call	printf               |
|  426 | bl       | bl	random                       | call	random               |
|  427 | bl       | bl	printf                       | call	printf               |
|  428 | bl       | bl	mergeSort                       | call	mergeSort               |
|  429 | bl       | bl	printf                       | call	printf               |
|  430 | bl       | bl	puts                       | call	puts               |
|  431 | bl       | bl	printf                       | call	printf               |
|  432 | bl       | bl	printf                       | call	printf               |
|  433 | ble      | ble	.L3                       | ble	x25, x0, .L3               |
|  434 | ble      | ble	.L8                       | ble	x25, x0, .L8               |
|  435 | ble      | ble	.L24                       | ble	x25, x0, .L24               |
|  436 | ble      | ble	.L5                       | ble	x25, x0, .L5               |
|  437 | ble      | ble	.L9                       | ble	x25, x0, .L9               |
|  438 | ble      | ble	.L14                       | ble	x25, x0, .L14               |
|  439 | ble      | ble	.L4                       | ble	x25, x0, .L4               |
|  440 | ble      | ble	.L16                       | ble	x25, x0, .L16               |
|  441 | ble      | ble	.L10                       | ble	x25, x0, .L10               |
|  442 | ble      | ble	.L7                       | ble	x25, x0, .L7               |
|  443 | blt      | blt	.L12                       | blt	x25, x0, .L12               |
|  444 | blt      | blt	.L10                       | blt	x25, x0, .L10               |
|  445 | blt      | blt	.L5                       | blt	x25, x0, .L5               |
|  446 | blt      | blt	.L21                       | blt	x25, x0, .L21               |
|  447 | blt      | blt	.L14                       | blt	x25, x0, .L14               |
|  448 | blt      | blt	.L3                       | blt	x25, x0, .L3               |
|  449 | bne      | bne	.L7                       | bne	x25, x0, .L7               |
|  450 | cmp      | cmp	x0, 0                       | addi	x25, x10, 0               |
|  451 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  452 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  453 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  454 | cmp      | cmp	w0, 9                       | addi	x25, x10, -9               |
|  455 | cmp      | cmp	x1, 0                       | addi	x25, x11, 0               |
|  456 | cmp      | cmp	x1, 0                       | addi	x25, x11, 0               |
|  457 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  458 | cmp      | cmp	x1, 0                       | addi	x25, x11, 0               |
|  459 | cmp      | cmp	w0, 0                       | addi	x25, x10, 0               |
|  460 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  461 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  462 | cmp      | cmp	w0, 999                       | addi	x25, x10, -999               |
|  463 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  464 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  465 | cmp      | cmp	x1, 0                       | addi	x25, x11, 0               |
|  466 | cmp      | cmp	w0, 999                       | addi	x25, x10, -999               |
|  467 | cmp      | cmp	w0, 100                       | addi	x25, x10, -100               |
|  468 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  469 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  470 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  471 | cmp      | cmp	w0, 999                       | addi	x25, x10, -999               |
|  472 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  473 | cmp      | cmp x10, x11          | sub	x25, x6, x7               |
|  474 | cmp      | cmp	w1, w0                       | sub	x25, x11, x10               |
|  475 | cmp      | cmp	w0, 999                       | addi	x25, x10, -999               |
|  476 | cmp      | cmp	w0, 999                       | addi	x25, x10, -999               |
|  477 | csel     | csel x0, x10, x11, LE | add	s11, x6, x0            |
|      |          |                       | ble	x25, x0, 999999f       |
|      |          |                       | add	s11, x7, x0            |
|      |          |                       | 999999:                    |
|      |          |                       | add	x10, x0, s11           |
|  478 | eor      | eor	x0, x1, x0                       | xor	x10, x11, x10               |
|  479 | eor      | eor	x1, x2, x1                       | xor	x11, x12, x11               |
|  480 | eor      | eor	x1, x3, x1                       | xor	x11, x13, x11               |
|  481 | eor      | eor	x1, x2, x1                       | xor	x11, x12, x11               |
|  482 | eor      | eor	x1, x2, x1                       | xor	x11, x12, x11               |
|  483 | fadd     | fadd	d0, d1, d0                       | fadd.d	f10, f11, f10               |
|  484 | fdiv     | fdiv	d0, d1, d0                       | fdiv.d	f10, f11, f10               |
|  485 | fmadd    | fmadd d0, d0, d1, d2  | fmadd.d	f10, f10, f11, f12               |
|  486 | fmov     | fmov	d0, x0                       | fmv.d.x	f10, x10               |
|  487 | fmov     | fmov	d2, x2                       | fmv.d.x	f12, x12               |
|  488 | fmov     | fmov	d0, x0                       | fmv.d.x	f10, x10               |
|  489 | fmov     | fmov	d1, x1                       | fmv.d.x	f11, x11               |
|  490 | fmov     | fmov	d1, x1                       | fmv.d.x	f11, x11               |
|  491 | fmov     | fmov	d0, x0                       | fmv.d.x	f10, x10               |
|  492 | fmov     | fmov	d0, x0                       | fmv.d.x	f10, x10               |
|  493 | fmov     | fmov	d1, x1                       | fmv.d.x	f11, x11               |
|  494 | fmov     | fmov	d0, x0                       | fmv.d.x	f10, x10               |
|  495 | fmov     | fmov	d0, x0                       | fmv.d.x	f10, x10               |
|  496 | fmov     | fmov	d2, x2                       | fmv.d.x	f12, x12               |
|  497 | fmov     | fmov	d1, x1                       | fmv.d.x	f11, x11               |
|  498 | fmov     | fmov	d2, x2                       | fmv.d.x	f12, x12               |
|  499 | fmov     | fmov	d2, x2                       | fmv.d.x	f12, x12               |
|  500 | fmsub    | fmsub d0, d0, d1, d2  | fnmsub.d	f10, f10, f11, f12               |
|  501 | fmul     | fmul	d0, d1, d0                       | fmul.d	f10, f11, f10               |
|  502 | fneg     | fneg d0, d0           | fneg.d	f10, f10               |
|  503 | fnmadd   | fnmadd d0, d0, d1, d2 | fnmadd.d	f10, f10, f11, f12               |
|  504 | fnmsub   | fnmsub d0, d0, d1, d2 | fmsub.d	f10, f10, f11, f12               |
|  505 | fsqrt    | fsqrt d0, d0          | fsqrt.d	f10, f10               |
|  506 | fsub     | fsub	d0, d1, d0                       | fsub.d	f10, f11, f10               |
|  507 | ldaddal  | ldaddal	w1, w1, [x0]                       | amoadd.w.aqrl	x11, x11, (x10)               |
|  508 | ldaddal  | ldaddal	w1, w1, [x0]                       | amoadd.w.aqrl	x11, x11, (x10)               |
|  509 | ldaddal  | ldaddal	w1, w2, [x0]                       | amoadd.w.aqrl	x12, x11, (x10)               |
|  510 | ldar     | ldar	w0, [x0]                       | lw	x10, 0(x10)                                                           |
|      |          |                       | fence	iorw,iorw # making implicit fence semantics explicit               |
|  511 | ldclral  | ldclral	w2, w2, [x0]                       | not	s11, x12                                |
|      |          |                       | amoand.w.aqrl	x12, s11, (x10)               |
|  512 | ldclral  | ldclral	w2, w2, [x0]                       | not	s11, x12                                |
|      |          |                       | amoand.w.aqrl	x12, s11, (x10)               |
|  513 | ldeoral  | ldeoral	w1, w2, [x0]                       | amoxor.w.aqrl	x12, x11, (x10)               |
|  514 | ldp      | ldp	x29, x30, [sp]                       | ld	x8, 0(x2)               |
|      |          |                       | ld	x1, 8(x2)               |
|  515 | ldp      | ldp	x29, x30, [sp]                       | ld	x8, 0(x2)               |
|      |          |                       | ld	x1, 8(x2)               |
|  516 | ldp      | ldp	x29, x30, [sp], 16                       | ld	x8, 0(x2)                  |
|      |          |                       | ld	x1, 8(x2)                  |
|      |          |                       | addi	x2, x2, 16               |
|  517 | ldp      | ldp	x29, x30, [sp], 32                       | ld	x8, 0(x2)                  |
|      |          |                       | ld	x1, 8(x2)                  |
|      |          |                       | addi	x2, x2, 32               |
|  518 | ldp      | ldp	x29, x30, [sp], 48                       | ld	x8, 0(x2)                  |
|      |          |                       | ld	x1, 8(x2)                  |
|      |          |                       | addi	x2, x2, 48               |
|  519 | ldp      | ldp	x29, x30, [sp], 128                       | ld	x8, 0(x2)                   |
|      |          |                       | ld	x1, 8(x2)                   |
|      |          |                       | addi	x2, x2, 128               |
|  520 | ldp      | ldp	x29, x30, [sp], 64                       | ld	x8, 0(x2)                  |
|      |          |                       | ld	x1, 8(x2)                  |
|      |          |                       | addi	x2, x2, 64               |
|  521 | ldp      | ldp	x29, x30, [sp], 48                       | ld	x8, 0(x2)                  |
|      |          |                       | ld	x1, 8(x2)                  |
|      |          |                       | addi	x2, x2, 48               |
|  522 | ldp      | ldp	x29, x30, [sp], 48                       | ld	x8, 0(x2)                  |
|      |          |                       | ld	x1, 8(x2)                  |
|      |          |                       | addi	x2, x2, 48               |
|  523 | ldp      | ldp	x29, x30, [sp]                       | ld	x8, 0(x2)               |
|      |          |                       | ld	x1, 8(x2)               |
|  524 | ldp      | ldp	x29, x30, [sp], 48                       | ld	x8, 0(x2)                  |
|      |          |                       | ld	x1, 8(x2)                  |
|      |          |                       | addi	x2, x2, 48               |
|  525 | ldp      | ldp	x29, x30, [sp], 48                       | ld	x8, 0(x2)                  |
|      |          |                       | ld	x1, 8(x2)                  |
|      |          |                       | addi	x2, x2, 48               |
|  526 | ldp      | ldp	x29, x30, [sp]                       | ld	x8, 0(x2)               |
|      |          |                       | ld	x1, 8(x2)               |
|  527 | ldp      | ldp	x29, x30, [sp], 32                       | ld	x8, 0(x2)                  |
|      |          |                       | ld	x1, 8(x2)                  |
|      |          |                       | addi	x2, x2, 32               |
|  528 | ldr      | ldr	x3, [x2, 7256]                       | li	s10, 7256                                            |
|      |          |                       | add	s10, x26, x12 # dealt with reg offset               |
|      |          |                       | ld	x13, 0(s10)                                          |
|  529 | ldr      | ldr	x1, [x1]                       | ld	x11, 0(x11)               |
|  530 | ldr      | ldr	x0, [x29, 40]                       | ld	x10, 40(x8)               |
|  531 | ldr      | ldr	w1, [x29, 44]                       | lw	x11, 44(x8)               |
|  532 | ldr      | ldr	w1, [x29, 28]                       | lw	x11, 28(x8)               |
|  533 | ldr      | ldr	x0, [x29, 32]                       | ld	x10, 32(x8)               |
|  534 | ldr      | ldr	x1, [x29, 32]                       | ld	x11, 32(x8)               |
|  535 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  536 | ldr      | ldr	x1, [x29, 32]                       | ld	x11, 32(x8)               |
|  537 | ldr      | ldr	x0, [x29, 40]                       | ld	x10, 40(x8)               |
|  538 | ldr      | ldr	x0, [x29, 48]                       | ld	x10, 48(x8)               |
|  539 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  540 | ldr      | ldr	x1, [x1, :got_lo12:__stack_chk_guard]                       | add	x11, x11, %lo(__stack_chk_guard)               |
|  541 | ldr      | ldr	x0, [x29, 40]                       | ld	x10, 40(x8)               |
|  542 | ldr      | ldr	w1, [x29, 28]                       | lw	x11, 28(x8)               |
|  543 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  544 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  545 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  546 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  547 | ldr      | ldr	x1, [x29, 32]                       | ld	x11, 32(x8)               |
|  548 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  549 | ldr      | ldr	w0, [x29, 16]                       | lw	x10, 16(x8)               |
|  550 | ldr      | ldr	x0, [x29, 40]                       | ld	x10, 40(x8)               |
|  551 | ldr      | ldr	x0, [x29, 40]                       | ld	x10, 40(x8)               |
|  552 | ldr      | ldr	x1, [x29, 32]                       | ld	x11, 32(x8)               |
|  553 | ldr      | ldr	x1, [x1, :got_lo12:__stack_chk_guard]                       | add	x11, x11, %lo(__stack_chk_guard)               |
|  554 | ldr      | ldr	x0, [x0, :got_lo12:__stack_chk_guard]                       | add	x10, x10, %lo(__stack_chk_guard)               |
|  555 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  556 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  557 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  558 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  559 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  560 | ldr      | ldr	w0, [x29, 16]                       | lw	x10, 16(x8)               |
|  561 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  562 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  563 | ldr      | ldr	x1, [x29, 32]                       | ld	x11, 32(x8)               |
|  564 | ldr      | ldr	x0, [x29, 40]                       | ld	x10, 40(x8)               |
|  565 | ldr      | ldr	x0, [x29, 40]                       | ld	x10, 40(x8)               |
|  566 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  567 | ldr      | ldr	w0, [x29, 16]                       | lw	x10, 16(x8)               |
|  568 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  569 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  570 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  571 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  572 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  573 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  574 | ldr      | ldr	w0, [x29, 16]                       | lw	x10, 16(x8)               |
|  575 | ldr      | ldr	x1, [x29, 32]                       | ld	x11, 32(x8)               |
|  576 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  577 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  578 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  579 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  580 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  581 | ldr      | ldr	x0, [x29, 40]                       | ld	x10, 40(x8)               |
|  582 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  583 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  584 | ldr      | ldr	x1, [x29, 32]                       | ld	x11, 32(x8)               |
|  585 | ldr      | ldr	w1, [x29, 28]                       | lw	x11, 28(x8)               |
|  586 | ldr      | ldr	x0, [x29, 40]                       | ld	x10, 40(x8)               |
|  587 | ldr      | ldr	w1, [x29, 28]                       | lw	x11, 28(x8)               |
|  588 | ldr      | ldr	w0, [x29, 24]                       | lw	x10, 24(x8)               |
|  589 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  590 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  591 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  592 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  593 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  594 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  595 | ldr      | ldr	x0, [x29, 56]                       | ld	x10, 56(x8)               |
|  596 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  597 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  598 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  599 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  600 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  601 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  602 | ldr      | ldr	w1, [x29, 28]                       | lw	x11, 28(x8)               |
|  603 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  604 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  605 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  606 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  607 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  608 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  609 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  610 | ldr      | ldr	x1, [x0]                       | ld	x11, 0(x10)               |
|  611 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  612 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  613 | ldr      | ldr	w1, [x29, 28]                       | lw	x11, 28(x8)               |
|  614 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  615 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  616 | ldr      | ldr	x1, [x29, 32]                       | ld	x11, 32(x8)               |
|  617 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  618 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  619 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  620 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  621 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  622 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  623 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  624 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  625 | ldr      | ldr	w0, [x29, 16]                       | lw	x10, 16(x8)               |
|  626 | ldr      | ldr	x0, [x29, 32]                       | ld	x10, 32(x8)               |
|  627 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  628 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  629 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  630 | ldr      | ldr	x1, [x1]                       | ld	x11, 0(x11)               |
|  631 | ldr      | ldr	x2, [x29, 20040]                       | li	s10, 20040                                          |
|      |          |                       | add	s10, x26, x8 # dealt with reg offset               |
|      |          |                       | ld	x12, 0(s10)                                         |
|  632 | ldr      | ldr	w0, [x29, 24]                       | lw	x10, 24(x8)               |
|  633 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  634 | ldr      | ldr	w0, [x29, 84]                       | lw	x10, 84(x8)               |
|  635 | ldr      | ldr	x0, [x29, 32]                       | ld	x10, 32(x8)               |
|  636 | ldr      | ldr	w0, [x29, 48]                       | lw	x10, 48(x8)               |
|  637 | ldr      | ldr	w0, [x29, 36]                       | lw	x10, 36(x8)               |
|  638 | ldr      | ldr	w0, [x29, 80]                       | lw	x10, 80(x8)               |
|  639 | ldr      | ldr	w1, [x29, 76]                       | lw	x11, 76(x8)               |
|  640 | ldr      | ldr	w0, [x29, 76]                       | lw	x10, 76(x8)               |
|  641 | ldr      | ldr	w0, [x29, 36]                       | lw	x10, 36(x8)               |
|  642 | ldr      | ldr	w1, [x0]                       | lw	x11, 0(x10)               |
|  643 | ldr      | ldr	x0, [x29, 96]                       | ld	x10, 96(x8)               |
|  644 | ldr      | ldr	w2, [x0]                       | lw	x12, 0(x10)               |
|  645 | ldr      | ldr	x1, [x29, 56]                       | ld	x11, 56(x8)               |
|  646 | ldr      | ldr	w0, [x29, 76]                       | lw	x10, 76(x8)               |
|  647 | ldr      | ldr	w1, [x29, 52]                       | lw	x11, 52(x8)               |
|  648 | ldr      | ldr	w0, [x29, 40]                       | lw	x10, 40(x8)               |
|  649 | ldr      | ldr	w1, [x0]                       | lw	x11, 0(x10)               |
|  650 | ldr      | ldr	w1, [x0]                       | lw	x11, 0(x10)               |
|  651 | ldr      | ldr	x1, [x0]                       | ld	x11, 0(x10)               |
|  652 | ldr      | ldr	x1, [x0]                       | ld	x11, 0(x10)               |
|  653 | ldr      | ldr	x1, [x0]                       | ld	x11, 0(x10)               |
|  654 | ldr      | ldr	x1, [x0]                       | ld	x11, 0(x10)               |
|  655 | ldr      | ldr	x1, [x1, :got_lo12:__stack_chk_guard]                       | add	x11, x11, %lo(__stack_chk_guard)               |
|  656 | ldr      | ldr	x2, [x29, 8040]                       | li	s10, 8040                                           |
|      |          |                       | add	s10, x26, x8 # dealt with reg offset               |
|      |          |                       | ld	x12, 0(s10)                                         |
|  657 | ldr      | ldr	x1, [x1]                       | ld	x11, 0(x11)               |
|  658 | ldr      | ldr	w1, [x0]                       | lw	x11, 0(x10)               |
|  659 | ldr      | ldr	w0, [x29, 72]                       | lw	x10, 72(x8)               |
|  660 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  661 | ldr      | ldr	x1, [x29, 56]                       | ld	x11, 56(x8)               |
|  662 | ldr      | ldr	x0, [x29, 112]                       | ld	x10, 112(x8)               |
|  663 | ldr      | ldr	w0, [x29, 76]                       | lw	x10, 76(x8)               |
|  664 | ldr      | ldr	w0, [x0]                       | lw	x10, 0(x10)               |
|  665 | ldr      | ldr	x0, [x1, x0]                       | add	s10, x10, x11 # dealt with reg offset               |
|      |          |                       | ld	x10, 0(s10)                                          |
|  666 | ldr      | ldr	w1, [x1, x2, lsl 2]                       | add	s10, x26, x11 # dealt with reg offset               |
|      |          |                       | lw	x11, 0(s10)                                          |
|  667 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  668 | ldr      | ldr	w1, [x1, x2, lsl 2]                       | slli	x26, x12, 2               |
|  669 | ldr      | ldr	x1, [x29, 96]                       | ld	x11, 96(x8)               |
|  670 | ldr      | ldr	x1, [x29, 56]                       | ld	x11, 56(x8)               |
|  671 | ldr      | ldr	x0, [x29, 16]                       | ld	x10, 16(x8)               |
|  672 | ldr      | ldr	w0, [x0, x2, lsl 2]                       | add	s10, x26, x10 # dealt with reg offset               |
|      |          |                       | lw	x10, 0(s10)                                          |
|  673 | ldr      | ldr	w0, [x0, x2, lsl 2]                       | slli	x26, x12, 2               |
|  674 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  675 | ldr      | ldr	x0, [x29, 112]                       | ld	x10, 112(x8)               |
|  676 | ldr      | ldr	w1, [x0, x1, lsl 2]                       | add	s10, x26, x10 # dealt with reg offset               |
|      |          |                       | lw	x11, 0(s10)                                          |
|  677 | ldr      | ldr	w1, [x0, x1, lsl 2]                       | slli	x26, x11, 2               |
|  678 | ldr      | ldr	w1, [x0]                       | lw	x11, 0(x10)               |
|  679 | ldr      | ldr	x0, [x29, 96]                       | ld	x10, 96(x8)               |
|  680 | ldr      | ldr	w1, [x0]                       | lw	x11, 0(x10)               |
|  681 | ldr      | ldr	w0, [x29, 52]                       | lw	x10, 52(x8)               |
|  682 | ldr      | ldr	w0, [x29, 84]                       | lw	x10, 84(x8)               |
|  683 | ldr      | ldr	w1, [x29, 72]                       | lw	x11, 72(x8)               |
|  684 | ldr      | ldr	w0, [x29, 72]                       | lw	x10, 72(x8)               |
|  685 | ldr      | ldr	w1, [x0]                       | lw	x11, 0(x10)               |
|  686 | ldr      | ldr	w2, [x0]                       | lw	x12, 0(x10)               |
|  687 | ldr      | ldr	x1, [x29, 56]                       | ld	x11, 56(x8)               |
|  688 | ldr      | ldr	w1, [x29, 24]                       | lw	x11, 24(x8)               |
|  689 | ldr      | ldr	d0, [x0]                       | fld	f10, 0(x10)               |
|  690 | ldr      | ldr	w1, [x29, 44]                       | lw	x11, 44(x8)               |
|  691 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  692 | ldr      | ldr	w0, [x29, 52]                       | lw	x10, 52(x8)               |
|  693 | ldr      | ldr	w1, [x29, 48]                       | lw	x11, 48(x8)               |
|  694 | ldr      | ldr	x0, [x29, 16]                       | ld	x10, 16(x8)               |
|  695 | ldr      | ldr	x1, [x29, 24]                       | ld	x11, 24(x8)               |
|  696 | ldr      | ldr	x2, [x29, 32]                       | ld	x12, 32(x8)               |
|  697 | ldr      | ldr	x1, [x0]                       | ld	x11, 0(x10)               |
|  698 | ldr      | ldr	x0, [x0, :got_lo12:__stack_chk_guard]                       | add	x10, x10, %lo(__stack_chk_guard)               |
|  699 | ldr      | ldr	x3, [x29, 32]                       | ld	x13, 32(x8)               |
|  700 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  701 | ldr      | ldr	x0, [x29, 16]                       | ld	x10, 16(x8)               |
|  702 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  703 | ldr      | ldr	x1, [x29, 24]                       | ld	x11, 24(x8)               |
|  704 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  705 | ldr      | ldr	x2, [x29, 32]                       | ld	x12, 32(x8)               |
|  706 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  707 | ldr      | ldr	x0, [x29, 16]                       | ld	x10, 16(x8)               |
|  708 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  709 | ldr      | ldr	x0, [x29, 16]                       | ld	x10, 16(x8)               |
|  710 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  711 | ldr      | ldr	x2, [x29, 32]                       | ld	x12, 32(x8)               |
|  712 | ldr      | ldr	x1, [x29, 24]                       | ld	x11, 24(x8)               |
|  713 | ldr      | ldr	x2, [x29, 32]                       | ld	x12, 32(x8)               |
|  714 | ldr      | ldr	w1, [x29, 28]                       | lw	x11, 28(x8)               |
|  715 | ldr      | ldr	w0, [x29, 48]                       | lw	x10, 48(x8)               |
|  716 | ldr      | ldr	w1, [x29, 28]                       | lw	x11, 28(x8)               |
|  717 | ldr      | ldr	d0, [x0]                       | fld	f10, 0(x10)               |
|  718 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  719 | ldr      | ldr	w0, [x29, 84]                       | lw	x10, 84(x8)               |
|  720 | ldr      | ldr	x0, [x0, :got_lo12:__stack_chk_guard]                       | add	x10, x10, %lo(__stack_chk_guard)               |
|  721 | ldr      | ldr	d0, [x0]                       | fld	f10, 0(x10)               |
|  722 | ldr      | ldr	d1, [x29, 16]                       | fld	f11, 16(x8)               |
|  723 | ldr      | ldr	x1, [x0]                       | ld	x11, 0(x10)               |
|  724 | ldr      | ldr	d0, [x29, 24]                       | fld	f10, 24(x8)               |
|  725 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  726 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  727 | ldr      | ldr	d1, [x29, 16]                       | fld	f11, 16(x8)               |
|  728 | ldr      | ldr	d0, [x29, 24]                       | fld	f10, 24(x8)               |
|  729 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  730 | ldr      | ldr	d1, [x29, 16]                       | fld	f11, 16(x8)               |
|  731 | ldr      | ldr	d0, [x29, 24]                       | fld	f10, 24(x8)               |
|  732 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  733 | ldr      | ldr	d1, [x29, 16]                       | fld	f11, 16(x8)               |
|  734 | ldr      | ldr	d0, [x29, 24]                       | fld	f10, 24(x8)               |
|  735 | ldr      | ldr	x0, [x1, x0]                       | add	s10, x10, x11 # dealt with reg offset               |
|      |          |                       | ld	x10, 0(s10)                                          |
|  736 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  737 | ldr      | ldr	x0, [x29, 16]                       | ld	x10, 16(x8)               |
|  738 | ldr      | ldr	x0, [x29, 32]                       | ld	x10, 32(x8)               |
|  739 | ldr      | ldr	x1, [x29, 24]                       | ld	x11, 24(x8)               |
|  740 | ldr      | ldr	w0, [x29, 80]                       | lw	x10, 80(x8)               |
|  741 | ldr      | ldr	x1, [x29, 112]                       | ld	x11, 112(x8)               |
|  742 | ldr      | ldr	x1, [x29, 40]                       | ld	x11, 40(x8)               |
|  743 | ldr      | ldr	w1, [x1, x2, lsl 2]                       | slli	x26, x12, 2               |
|  744 | ldr      | ldr	w2, [x29, 44]                       | lw	x12, 44(x8)               |
|  745 | ldr      | ldr	w1, [sp, 24]                       | lw	x11, 24(x2)               |
|  746 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  747 | ldr      | ldr	w0, [sp, 20]                       | lw	x10, 20(x2)               |
|  748 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  749 | ldr      | ldr	w1, [x29, 16]                       | lw	x11, 16(x8)               |
|  750 | ldr      | ldr	w0, [x29, 16]                       | lw	x10, 16(x8)               |
|  751 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  752 | ldr      | ldr	w0, [sp, 20]                       | lw	x10, 20(x2)               |
|  753 | ldr      | ldr	x0, [x29, 24]                       | ld	x10, 24(x8)               |
|  754 | ldr      | ldr	w0, [x0]                       | lw	x10, 0(x10)               |
|  755 | ldr      | ldr	x19, [sp, 16]                       | ld	x18, 16(x2)               |
|  756 | ldr      | ldr	x1, [x1]                       | ld	x11, 0(x11)               |
|  757 | ldr      | ldr	x0, [x0]                       | ld	x10, 0(x10)               |
|  758 | ldr      | ldr	x1, [x29, 120]                       | ld	x11, 120(x8)               |
|  759 | ldr      | ldr	x0, [x0, :got_lo12:__stack_chk_guard]                       | add	x10, x10, %lo(__stack_chk_guard)               |
|  760 | ldr      | ldr	x1, [x1, :got_lo12:__stack_chk_guard]                       | add	x11, x11, %lo(__stack_chk_guard)               |
|  761 | ldr      | ldr	w0, [x29, 84]                       | lw	x10, 84(x8)               |
|  762 | ldr      | ldr	w1, [x29, 72]                       | lw	x11, 72(x8)               |
|  763 | ldr      | ldr	x0, [x0, :got_lo12:__stack_chk_guard]                       | add	x10, x10, %lo(__stack_chk_guard)               |
|  764 | ldr      | ldr	w0, [x29, 40]                       | lw	x10, 40(x8)               |
|  765 | ldr      | ldr	x1, [x0]                       | ld	x11, 0(x10)               |
|  766 | ldr      | ldr	x0, [x29, 32]                       | ld	x10, 32(x8)               |
|  767 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  768 | ldr      | ldr	w1, [x29, 28]                       | lw	x11, 28(x8)               |
|  769 | ldr      | ldr	x0, [x29, 24]                       | ld	x10, 24(x8)               |
|  770 | ldr      | ldr	w2, [x29, 16]                       | lw	x12, 16(x8)               |
|  771 | ldr      | ldr	x2, [x0]                       | ld	x12, 0(x10)               |
|  772 | ldr      | ldr	x0, [x0, :got_lo12:__stack_chk_guard]                       | add	x10, x10, %lo(__stack_chk_guard)               |
|  773 | ldr      | ldr	x0, [sp, 8]                       | ld	x10, 8(x2)               |
|  774 | ldr      | ldr	w0, [x0]                       | lw	x10, 0(x10)               |
|  775 | ldr      | ldr	w0, [sp, 24]                       | lw	x10, 24(x2)               |
|  776 | ldr      | ldr	w1, [sp, 24]                       | lw	x11, 24(x2)               |
|  777 | ldr      | ldr	w1, [sp, 24]                       | lw	x11, 24(x2)               |
|  778 | ldr      | ldr	w0, [x29, 20]                       | lw	x10, 20(x8)               |
|  779 | ldr      | ldr	w1, [x29, 44]                       | lw	x11, 44(x8)               |
|  780 | ldr      | ldr	w1, [sp, 24]                       | lw	x11, 24(x2)               |
|  781 | ldr      | ldr	w0, [x29, 44]                       | lw	x10, 44(x8)               |
|  782 | ldr      | ldr	w1, [x0]                       | lw	x11, 0(x10)               |
|  783 | ldr      | ldr	x1, [x29, 24]                       | ld	x11, 24(x8)               |
|  784 | ldr      | ldr	w0, [sp, 24]                       | lw	x10, 24(x2)               |
|  785 | ldr      | ldr	w1, [sp, 24]                       | lw	x11, 24(x2)               |
|  786 | ldr      | ldr	w1, [sp, 12]                       | lw	x11, 12(x2)               |
|  787 | ldr      | ldr	w1, [sp, 24]                       | lw	x11, 24(x2)               |
|  788 | ldr      | ldr	x0, [x29, 24]                       | ld	x10, 24(x8)               |
|  789 | ldr      | ldr	w1, [x29, 20]                       | lw	x11, 20(x8)               |
|  790 | ldr      | ldr	w2, [x29, 44]                       | lw	x12, 44(x8)               |
|  791 | ldr      | ldr	w3, [x29, 16]                       | lw	x13, 16(x8)               |
|  792 | ldr      | ldr	w1, [sp, 24]                       | lw	x11, 24(x2)               |
|  793 | ldr      | ldr	x0, [x29, 24]                       | ld	x10, 24(x8)               |
|  794 | ldr      | ldr	w0, [x29, 44]                       | lw	x10, 44(x8)               |
|  795 | ldr      | ldr	w0, [x29, 68]                       | lw	x10, 68(x8)               |
|  796 | ldr      | ldr	x2, [x29, 8040]                       | li	s10, 8040                                           |
|      |          |                       | add	s10, x26, x8 # dealt with reg offset               |
|      |          |                       | ld	x12, 0(s10)                                         |
|  797 | ldr      | ldr	w1, [x0]                       | lw	x11, 0(x10)               |
|  798 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  799 | ldr      | ldr	w1, [x29, 72]                       | lw	x11, 72(x8)               |
|  800 | ldr      | ldr	w1, [x29, 76]                       | lw	x11, 76(x8)               |
|  801 | ldr      | ldr	w0, [x29, 68]                       | lw	x10, 68(x8)               |
|  802 | ldr      | ldr	x1, [x29, 56]                       | ld	x11, 56(x8)               |
|  803 | ldr      | ldr	w0, [x29, 76]                       | lw	x10, 76(x8)               |
|  804 | ldr      | ldr	x1, [x29, 112]                       | ld	x11, 112(x8)               |
|  805 | ldr      | ldr	x3, [x29, 32]                       | ld	x13, 32(x8)               |
|  806 | ldr      | ldr	w1, [x29, 76]                       | lw	x11, 76(x8)               |
|  807 | ldr      | ldr	w0, [x29, 68]                       | lw	x10, 68(x8)               |
|  808 | ldr      | ldr	w1, [x29, 40]                       | lw	x11, 40(x8)               |
|  809 | ldr      | ldr	w0, [x29, 80]                       | lw	x10, 80(x8)               |
|  810 | ldr      | ldr	w1, [x1, x2, lsl 2]                       | add	s10, x26, x11 # dealt with reg offset               |
|      |          |                       | lw	x11, 0(s10)                                          |
|  811 | ldr      | ldr	w0, [x29, 72]                       | lw	x10, 72(x8)               |
|  812 | ldr      | ldr	w1, [x1, x2, lsl 2]                       | slli	x26, x12, 2               |
|  813 | ldr      | ldr	w0, [x29, 28]                       | lw	x10, 28(x8)               |
|  814 | ldr      | ldr	w0, [x29, 40]                       | lw	x10, 40(x8)               |
|  815 | ldr      | ldr	x1, [x29, 56]                       | ld	x11, 56(x8)               |
|  816 | ldr      | ldr	w1, [x1, x2, lsl 2]                       | slli	x26, x12, 2               |
|  817 | ldr      | ldr	x1, [x29, 96]                       | ld	x11, 96(x8)               |
|  818 | ldr      | ldr	w1, [x1, x2, lsl 2]                       | add	s10, x26, x11 # dealt with reg offset               |
|      |          |                       | lw	x11, 0(s10)                                          |
|  819 | ldr      | ldr	w1, [x1, x2, lsl 2]                       | add	s10, x26, x11 # dealt with reg offset               |
|      |          |                       | lw	x11, 0(s10)                                          |
|  820 | ldr      | ldr	w0, [x29, 72]                       | lw	x10, 72(x8)               |
|  821 | ldr      | ldr	w0, [x29, 80]                       | lw	x10, 80(x8)               |
|  822 | ldrsh    | ldrsh	w0, [x1, x0]                       | add	s10, x10, x11 # dealt with reg offset               |
|      |          |                       | lh	x10, 0(s10)                                          |
|  823 | ldrsw    | ldrsw	x1, [x29, 76]                       | lw	x11, 76(x8)               |
|  824 | ldrsw    | ldrsw	x0, [x29, 68]                       | lw	x10, 68(x8)               |
|  825 | ldrsw    | ldrsw	x0, [x29, 28]                       | lw	x10, 28(x8)               |
|  826 | ldrsw    | ldrsw	x2, [x29, 76]                       | lw	x12, 76(x8)               |
|  827 | ldrsw    | ldrsw	x0, [x29, 44]                       | lw	x10, 44(x8)               |
|  828 | ldrsw    | ldrsw	x2, [x29, 72]                       | lw	x12, 72(x8)               |
|  829 | ldrsw    | ldrsw	x0, [x29, 28]                       | lw	x10, 28(x8)               |
|  830 | ldrsw    | ldrsw	x0, [x29, 28]                       | lw	x10, 28(x8)               |
|  831 | ldrsw    | ldrsw	x0, [x29, 28]                       | lw	x10, 28(x8)               |
|  832 | ldrsw    | ldrsw	x0, [x29, 68]                       | lw	x10, 68(x8)               |
|  833 | ldrsw    | ldrsw	x0, [x29, 28]                       | lw	x10, 28(x8)               |
|  834 | ldrsw    | ldrsw	x0, [x29, 16]                       | lw	x10, 16(x8)               |
|  835 | ldrsw    | ldrsw	x1, [x29, 72]                       | lw	x11, 72(x8)               |
|  836 | ldrsw    | ldrsw	x2, [x29, 72]                       | lw	x12, 72(x8)               |
|  837 | ldrsw    | ldrsw	x0, [x29, 24]                       | lw	x10, 24(x8)               |
|  838 | ldrsw    | ldrsw	x1, [x29, 76]                       | lw	x11, 76(x8)               |
|  839 | ldrsw    | ldrsw	x2, [x29, 76]                       | lw	x12, 76(x8)               |
|  840 | ldrsw    | ldrsw	x0, [x29, 68]                       | lw	x10, 68(x8)               |
|  841 | ldrsw    | ldrsw	x2, [x29, 72]                       | lw	x12, 72(x8)               |
|  842 | ldrsw    | ldrsw	x0, [x29, 68]                       | lw	x10, 68(x8)               |
|  843 | ldsetal  | ldsetal	w1, w2, [x0]                       | amoor.w.aqrl	x12, x11, (x10)               |
|  844 | ldsmaxal | ldsmaxal x1, x1, [x0] | amomax.d.aqrl	x11, x11, (x10)               |
|  845 | ldsminal | ldsminal x1, x1, [x0] | amomin.d.aqrl	x11, x11, (x10)               |
|  846 | ldumaxal | ldumaxal x1, x1, [x0] | amomaxu.d.aqrl	x11, x11, (x10)               |
|  847 | lduminal | lduminal x1, x1, [x0] | amominu.d.aqrl	x11, x11, (x10)               |
|  848 | lsl      | lsl	x0, x0, 1                       | slli	x10, x10, 1               |
|  849 | lsl      | lsl	x0, x0, 3                       | slli	x10, x10, 3               |
|  850 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  851 | lsl      | lsl	x0, x0, 3                       | slli	x10, x10, 3               |
|  852 | lsl      | lsl	x0, x0, 3                       | slli	x10, x10, 3               |
|  853 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  854 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  855 | lsl      | lsl	x10, x18, 5                       | ld	x22, 8(x21) # load of mmapped register               |
|      |          |                       | slli	x6, x22, 5                                         |
|  856 | lsl      | lsl	x11, x19, 5                       | slli	x7, x18, 5               |
|  857 | lsl      | lsl	x0, x0, 35                       | slli	x10, x10, 35               |
|  858 | lsl      | lsl	x0, x0, 4                       | slli	x10, x10, 4               |
|  859 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  860 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  861 | lsl      | lsl	x0, x0, 34                       | slli	x10, x10, 34               |
|  862 | lsl      | lsl	x4, x12, 5                       | slli	x14, x28, 5               |
|  863 | lsl      | lsl	x5, x13, 5                       | slli	x15, x29, 5               |
|  864 | lsl      | lsl	w0, w0, 1                       | slliw	x10, x10, 1               |
|  865 | lsl      | lsl	x6, x14, 5                       | slli	x16, x30, 5               |
|  866 | lsl      | lsl	x7, x15, 5                       | slli	x17, x31, 5               |
|  867 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  868 | lsl      | lsl	x0, x0, 1                       | slli	x10, x10, 1               |
|  869 | lsl      | lsl	x0, x0, 35                       | slli	x10, x10, 35               |
|  870 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  871 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  872 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  873 | lsl      | lsl	x0, x0, 4                       | slli	x10, x10, 4               |
|  874 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  875 | lsl      | lsl	x8, x16, 5                       | slli	x9, x27, 5               |
|  876 | lsl      | lsl	x0, x0, 34                       | slli	x10, x10, 34               |
|  877 | lsl      | lsl	x9, x17, 5                       | ld	x22, 0(x21) # load of mmapped register               |
|      |          |                       | slli	x5, x22, 5                                         |
|  878 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  879 | lsl      | lsl	x0, x0, 3                       | slli	x10, x10, 3               |
|  880 | lsl      | lsl	x0, x0, 2                       | slli	x10, x10, 2               |
|  881 | lsr      | lsr	x0, x0, 2                       | srli	x10, x10, 2               |
|  882 | lsr      | lsr	x0, x0, 2                       | srli	x10, x10, 2               |
|  883 | lsr      | lsr	x0, x0, 4                       | srli	x10, x10, 4               |
|  884 | lsr      | lsr	x0, x0, 4                       | srli	x10, x10, 4               |
|  885 | lsr      | lsr	x1, x16, 59                       | srli	x11, x27, 59               |
|  886 | lsr      | lsr	x1, x12, 59                       | srli	x11, x28, 59               |
|  887 | lsr      | lsr	w1, w0, 31                       | srliw	x11, x10, 31               |
|  888 | lsr      | lsr	x1, x14, 59                       | srli	x11, x30, 59               |
|  889 | lsr      | lsr	x1, x18, 59                       | ld	x22, 8(x21) # load of mmapped register               |
|      |          |                       | srli	x11, x22, 59                                       |
|  890 | mov      | mov	x1,0                       | li	x11, 0               |
|  891 | mov      | mov	w0, 0                       | li	x10, 0               |
|  892 | mov      | mov	x0, 4                       | li	x10, 4               |
|  893 | mov      | mov	x2, x1                       | mv	x12, x11               |
|  894 | mov      | mov	w1, 0                       | li	x11, 0               |
|  895 | mov      | mov	w0, 2                       | li	x10, 2               |
|  896 | mov      | mov	w2, 1                       | li	x12, 1               |
|  897 | mov      | mov	w0, 0                       | li	x10, 0               |
|  898 | mov      | mov	x2, x0                       | mv	x12, x10               |
|  899 | mov      | mov	x1, 0                       | li	x11, 0               |
|  900 | mov      | mov	x0, x4                       | mv	x10, x14               |
|  901 | mov      | mov	w0, 10000                       | li	x10, 10000               |
|  902 | mov      | mov	w1, 10000                       | li	x11, 10000               |
|  903 | mov      | mov	w0, 2                       | li	x10, 2               |
|  904 | mov      | mov	w0, 10000                       | li	x10, 10000               |
|  905 | mov      | mov	x0, 1                       | li	x10, 1               |
|  906 | mov      | mov	w0, 10                       | li	x10, 10               |
|  907 | mov      | mov	x1, 0                       | li	x11, 0               |
|  908 | mov      | mov	x16, 20048                       | li	x27, 20048               |
|  909 | mov      | mov	w0, 99                       | li	x10, 99               |
|  910 | mov      | mov	w0, 10                       | li	x10, 10               |
|  911 | mov      | mov	x1, 20002                       | li	x11, 20002               |
|  912 | mov      | mov	x0, 1                       | li	x10, 1               |
|  913 | mov      | mov	w0, 0                       | li	x10, 0               |
|  914 | mov      | mov	w1, 1                       | li	x11, 1               |
|  915 | mov      | mov	x16, 8048                       | li	x27, 8048               |
|  916 | mov      | mov	x1, 0                       | li	x11, 0               |
|  917 | mov      | mov	x16, 40032                       | li	x27, 40032               |
|  918 | mov      | mov	w2, w0                       | mv	x12, x10               |
|  919 | mov      | mov	w1, 1                       | li	x11, 1               |
|  920 | mov      | mov	w0, 10                       | li	x10, 10               |
|  921 | mov      | mov	w0, 9999                       | li	x10, 9999               |
|  922 | mov      | mov	w1, 1000                       | li	x11, 1000               |
|  923 | mov      | mov	w0, 10000                       | li	x10, 10000               |
|  924 | mov      | mov	w1, w0                       | mv	x11, x10               |
|  925 | mov      | mov	w2, w1                       | mv	x12, x11               |
|  926 | mov      | mov	x1,0                       | li	x11, 0               |
|  927 | mov      | mov	w1, 1000                       | li	x11, 1000               |
|  928 | mov      | mov	w2, w1                       | mv	x12, x11               |
|  929 | mov      | mov	w1, 0                       | li	x11, 0               |
|  930 | mov      | mov	w1, w0                       | mv	x11, x10               |
|  931 | mov      | mov	w0, 0                       | li	x10, 0               |
|  932 | mov      | mov	w1, w0                       | mv	x11, x10               |
|  933 | mov      | mov	x0, 1                       | li	x10, 1               |
|  934 | mov      | mov	x0, 0                       | li	x10, 0               |
|  935 | mov      | mov	x16, 40032                       | li	x27, 40032               |
|  936 | mov      | mov	x16, 20048                       | li	x27, 20048               |
|  937 | mov      | mov	x16, 8048                       | li	x27, 8048               |
|  938 | mov      | mov	x0, 1                       | li	x10, 1               |
|  939 | mov      | mov	w2, w1                       | mv	x12, x11               |
|  940 | mov      | mov	sp, x3                       | mv	x2, x13               |
|  941 | mov      | mov	w0, 0                       | li	x10, 0               |
|  942 | mov      | mov	x0, sp                       | mv	x10, x2               |
|  943 | mov      | mov	x16, 8048                       | li	x27, 8048               |
|  944 | mov      | mov	x2,0                       | li	x12, 0               |
|  945 | mov      | mov	x0, sp                       | mv	x10, x2               |
|  946 | mov      | mov	x1,0                       | li	x11, 0               |
|  947 | mov      | mov	x17, 0                       | ld	x22, 0(x21) # load of mmapped register                |
|      |          |                       | li	x22, 0                                                |
|      |          |                       | sd	x22, 0(x21) # store of mmapped register               |
|  948 | mov      | mov	x16, x1                       | mv	x27, x11               |
|  949 | mov      | mov	x1, 0                       | li	x11, 0               |
|  950 | mov      | mov	x19, 0                       | li	x18, 0               |
|  951 | mov      | mov	x18, x1                       | ld	x22, 8(x21) # load of mmapped register                |
|      |          |                       | mv	x22, x11                                              |
|      |          |                       | sd	x22, 8(x21) # store of mmapped register               |
|  952 | mov      | mov	x14, x1                       | mv	x30, x11               |
|  953 | mov      | mov	x0, 4                       | li	x10, 4               |
|  954 | mov      | mov	w0, 99                       | li	x10, 99               |
|  955 | mov      | mov	w0, 10                       | li	x10, 10               |
|  956 | mov      | mov	x3, x0                       | mv	x13, x10               |
|  957 | mov      | mov	x0, sp                       | mv	x10, x2               |
|  958 | mov      | mov	x1,0                       | li	x11, 0               |
|  959 | mov      | mov	x2, x0                       | mv	x12, x10               |
|  960 | mov      | mov	x1, 0                       | li	x11, 0               |
|  961 | mov      | mov	x0, x4                       | mv	x10, x14               |
|  962 | mov      | mov	w0, 0                       | li	x10, 0               |
|  963 | mov      | mov	w0, 0                       | li	x10, 0               |
|  964 | mov      | mov	w0, 0                       | li	x10, 0               |
|  965 | mov      | mov	w0, 1234                       | li	x10, 1234               |
|  966 | mov      | mov x11, x1           | mv	x7, x11               |
|  967 | mov      | mov	w0, 99                       | li	x10, 99               |
|  968 | mov      | mov	w0, 32                       | li	x10, 32               |
|  969 | mov      | mov	w0, 35                       | li	x10, 35               |
|  970 | mov      | mov	x13, 0                       | li	x29, 0               |
|  971 | mov      | mov	x12, x1                       | mv	x28, x11               |
|  972 | mov      | mov	x16, 8048                       | li	x27, 8048               |
|  973 | mov      | mov	x15, 0                       | li	x31, 0               |
|  974 | mov      | mov	x0, 0                       | li	x10, 0               |
|  975 | mov      | mov	w0, 10                       | li	x10, 10               |
|  976 | mov      | mov x10, x0           | mv	x6, x10               |
|  977 | mov      | mov	w0, 0                       | li	x10, 0               |
|  978 | mov      | mov	w0, 10                       | li	x10, 10               |
|  979 | mov      | mov	w0, 99                       | li	x10, 99               |
|  980 | mul      | mul	w1, w1, w0                       | mulw	x11, x11, x10               |
|  981 | mul      | mul	x1, x2, x1                       | mul	x11, x12, x11               |
|  982 | mul      | mul	w1, w2, w1                       | mulw	x11, x12, x11               |
|  983 | mul      | mul	x1, x1, x0                       | mul	x11, x11, x10               |
|  984 | mul      | mul	w1, w2, w1                       | mulw	x11, x12, x11               |
|  985 | mul      | mul	w1, w2, w1                       | mulw	x11, x12, x11               |
|  986 | mul      | mul	x1, x1, x0                       | mul	x11, x11, x10               |
|  987 | mul      | mul	w1, w1, w0                       | mulw	x11, x11, x10               |
|  988 | mul      | mul	w1, w1, w0                       | mulw	x11, x11, x10               |
|  989 | mul      | mul	w1, w1, w0                       | mulw	x11, x11, x10               |
|  990 | mul      | mul	w1, w2, w1                       | mulw	x11, x12, x11               |
|  991 | mul      | mul	w1, w2, w1                       | mulw	x11, x12, x11               |
|  992 | mul      | mul	w1, w1, w0                       | mulw	x11, x11, x10               |
|  993 | mul      | mul	x1, x2, x1                       | mul	x11, x12, x11               |
|  994 | mvn      | mvn	w2, w2                       | mv	x12, x12                |
|      |          |                       | not	x12, x12               |
|  995 | mvn      | mvn	w2, w2                       | mv	x12, x12                |
|      |          |                       | not	x12, x12               |
|  996 | neg      | neg	w0, w0                       | sub	x10, x0, x10               |
|  997 | neg      | neg	w0, w0                       | sub	x10, x0, x10               |
|  998 | nop      | nop                   | nop           |
|  999 | nop      | nop                   | nop           |
| 1000 | nop      | nop                   | nop           |
| 1001 | nop      | nop                   | nop           |
| 1002 | nop      | nop                   | nop           |
| 1003 | nop      | nop                   | nop           |
| 1004 | orr      | orr	x5, x1, x5                       | or	x15, x11, x15               |
| 1005 | orr      | orr	x11, x1, x11                       | or	x7, x11, x7               |
| 1006 | orr      | orr	x7, x1, x7                       | or	x17, x11, x17               |
| 1007 | orr      | orr	x9, x1, x9                       | or	x5, x11, x5               |
| 1008 | ret      | ret                   | ret           |
| 1009 | ret      | ret                   | ret           |
| 1010 | ret      | ret                   | ret           |
| 1011 | ret      | ret                   | ret           |
| 1012 | ret      | ret                   | ret           |
| 1013 | ret      | ret                   | ret           |
| 1014 | ret      | ret                   | ret           |
| 1015 | ret      | ret                   | ret           |
| 1016 | ret      | ret                   | ret           |
| 1017 | ret      | ret                   | ret           |
| 1018 | ret      | ret                   | ret           |
| 1019 | ret      | ret                   | ret           |
| 1020 | ret      | ret                   | ret           |
| 1021 | ret      | ret                   | ret           |
| 1022 | ret      | ret                   | ret           |
| 1023 | ret      | ret                   | ret           |
| 1024 | sdiv     | sdiv	w2, w0, w1                       | divw	x12, x10, x11               |
| 1025 | sdiv     | sdiv	w1, w1, w0                       | divw	x11, x11, x10               |
| 1026 | sdiv     | sdiv	x1, x1, x0                       | div	x11, x11, x10               |
| 1027 | sdiv     | sdiv	w1, w1, w0                       | divw	x11, x11, x10               |
| 1028 | sdiv     | sdiv	x2, x0, x1                       | div	x12, x10, x11               |
| 1029 | sdiv     | sdiv	x1, x1, x0                       | div	x11, x11, x10               |
| 1030 | sdiv     | sdiv	w2, w0, w1                       | divw	x12, x10, x11               |
| 1031 | sdiv     | sdiv	w1, w1, w0                       | divw	x11, x11, x10               |
| 1032 | sdiv     | sdiv	x2, x0, x1                       | div	x12, x10, x11               |
| 1033 | sdiv     | sdiv	w2, w0, w1                       | divw	x12, x10, x11               |
| 1034 | stlr     | stlr	w1, [x0]                       | fence	iorw,iorw  # making implicit fence semantics explicit               |
|      |          |                       | sw	x11, 0(x10)                                                            |
| 1035 | stp      | stp	x29, x30, [sp, -64]!                       | sd	x8, -64(x2)                 |
|      |          |                       | sd	x1, -56(x2)                 |
|      |          |                       | addi	x2, x2, -64               |
| 1036 | stp      | stp	x29, x30, [sp]                       | sd	x8, 0(x2)               |
|      |          |                       | sd	x1, 8(x2)               |
| 1037 | stp      | stp	x29, x30, [sp]                       | sd	x8, 0(x2)               |
|      |          |                       | sd	x1, 8(x2)               |
| 1038 | stp      | stp	x29, x30, [sp, -16]!                       | sd	x8, -16(x2)                 |
|      |          |                       | sd	x1, -8(x2)                  |
|      |          |                       | addi	x2, x2, -16               |
| 1039 | stp      | stp	x29, x30, [sp]                       | sd	x8, 0(x2)               |
|      |          |                       | sd	x1, 8(x2)               |
| 1040 | stp      | stp	x29, x30, [sp, -48]!                       | sd	x8, -48(x2)                 |
|      |          |                       | sd	x1, -40(x2)                 |
|      |          |                       | addi	x2, x2, -48               |
| 1041 | stp      | stp	x29, x30, [sp, -128]!                       | sd	x8, -128(x2)                 |
|      |          |                       | sd	x1, -120(x2)                 |
|      |          |                       | addi	x2, x2, -128               |
| 1042 | stp      | stp	x29, x30, [sp, -48]!                       | sd	x8, -48(x2)                 |
|      |          |                       | sd	x1, -40(x2)                 |
|      |          |                       | addi	x2, x2, -48               |
| 1043 | stp      | stp	x29, x30, [sp, -48]!                       | sd	x8, -48(x2)                 |
|      |          |                       | sd	x1, -40(x2)                 |
|      |          |                       | addi	x2, x2, -48               |
| 1044 | stp      | stp	x29, x30, [sp, -48]!                       | sd	x8, -48(x2)                 |
|      |          |                       | sd	x1, -40(x2)                 |
|      |          |                       | addi	x2, x2, -48               |
| 1045 | stp      | stp	x29, x30, [sp, -32]!                       | sd	x8, -32(x2)                 |
|      |          |                       | sd	x1, -24(x2)                 |
|      |          |                       | addi	x2, x2, -32               |
| 1046 | stp      | stp	x29, x30, [sp, -48]!                       | sd	x8, -48(x2)                 |
|      |          |                       | sd	x1, -40(x2)                 |
|      |          |                       | addi	x2, x2, -48               |
| 1047 | stp      | stp	x29, x30, [sp]                       | sd	x8, 0(x2)               |
|      |          |                       | sd	x1, 8(x2)               |
| 1048 | stp      | stp	x29, x30, [sp, -32]!                       | sd	x8, -32(x2)                 |
|      |          |                       | sd	x1, -24(x2)                 |
|      |          |                       | addi	x2, x2, -32               |
| 1049 | str      | str	w0, [x29, 84]                       | sw	x10, 84(x8)               |
| 1050 | str      | str	w0, [x29, 76]                       | sw	x10, 76(x8)               |
| 1051 | str      | str	x0, [x29, 32]                       | sd	x10, 32(x8)               |
| 1052 | str      | str	w1, [x0]                       | sw	x11, 0(x10)               |
| 1053 | str      | str	w0, [x29, 68]                       | sw	x10, 68(x8)               |
| 1054 | str      | str	x1, [x29, 88]                       | sd	x11, 88(x8)               |
| 1055 | str      | str	w0, [x29, 80]                       | sw	x10, 80(x8)               |
| 1056 | str      | str	wzr, [x29, 72]                       | sw	x0, 72(x8)               |
| 1057 | str      | str	wzr, [x29, 76]                       | sw	x0, 76(x8)               |
| 1058 | str      | str	w1, [x0]                       | sw	x11, 0(x10)               |
| 1059 | str      | str	w0, [x29, 76]                       | sw	x10, 76(x8)               |
| 1060 | str      | str	w1, [x0]                       | sw	x11, 0(x10)               |
| 1061 | str      | str	w2, [x0, x1, lsl 2]                       | add	s10, x26, x10 # dealt with reg offset               |
|      |          |                       | sw	x12, 0(s10)                                          |
| 1062 | str      | str	x1, [x29, 8040]                       | li	s10, 8040                                           |
|      |          |                       | add	s10, x26, x8 # dealt with reg offset               |
|      |          |                       | sd	x11, 0(s10)                                         |
| 1063 | str      | str	x0, [x29, 96]                       | sd	x10, 96(x8)               |
| 1064 | str      | str	x1, [x29, 104]                       | sd	x11, 104(x8)               |
| 1065 | str      | str	x0, [x29, 112]                       | sd	x10, 112(x8)               |
| 1066 | str      | str	wzr, [x29, 76]                       | sw	x0, 76(x8)               |
| 1067 | str      | str	x1, [x29, 120]                       | sd	x11, 120(x8)               |
| 1068 | str      | str	w2, [x0, x1, lsl 2]                       | slli	x26, x11, 2               |
| 1069 | str      | str	w2, [x0, x1, lsl 2]                       | slli	x26, x11, 2               |
| 1070 | str      | str	wzr, [x29, 72]                       | sw	x0, 72(x8)               |
| 1071 | str      | str	w2, [x0, x1, lsl 2]                       | add	s10, x26, x10 # dealt with reg offset               |
|      |          |                       | sw	x12, 0(s10)                                          |
| 1072 | str      | str	w0, [x29, 36]                       | sw	x10, 36(x8)               |
| 1073 | str      | str	wzr, [x29, 28]                       | sw	x0, 28(x8)               |
| 1074 | str      | str	w0, [x29, 72]                       | sw	x10, 72(x8)               |
| 1075 | str      | str	d0, [x29, 40]                       | fsd	f10, 40(x8)               |
| 1076 | str      | str	w2, [x29, 48]                       | sw	x12, 48(x8)               |
| 1077 | str      | str	wzr, [x29, 28]                       | sw	x0, 28(x8)               |
| 1078 | str      | str	w0, [x29, 24]                       | sw	x10, 24(x8)               |
| 1079 | str      | str	w0, [x29, 20]                       | sw	x10, 20(x8)               |
| 1080 | str      | str	w0, [x29, 28]                       | sw	x10, 28(x8)               |
| 1081 | str      | str	wzr, [x29, 28]                       | sw	x0, 28(x8)               |
| 1082 | str      | str	w0, [x29, 28]                       | sw	x10, 28(x8)               |
| 1083 | str      | str	w1, [x0]                       | sw	x11, 0(x10)               |
| 1084 | str      | str	x0, [x29, 32]                       | sd	x10, 32(x8)               |
| 1085 | str      | str	wzr, [x29, 28]                       | sw	x0, 28(x8)               |
| 1086 | str      | str	x1, [x29, 8040]                       | li	s10, 8040                                           |
|      |          |                       | add	s10, x26, x8 # dealt with reg offset               |
|      |          |                       | sd	x11, 0(s10)                                         |
| 1087 | str      | str	w0, [sp, 20]                       | sw	x10, 20(x2)               |
| 1088 | str      | str	wzr, [sp, 20]                       | sw	x0, 20(x2)               |
| 1089 | str      | str	w0, [sp, 28]                       | sw	x10, 28(x2)               |
| 1090 | str      | str	w0, [sp, 24]                       | sw	x10, 24(x2)               |
| 1091 | str      | str	x0, [sp, 8]                       | sd	x10, 8(x2)               |
| 1092 | str      | str	w0, [x29, 28]                       | sw	x10, 28(x8)               |
| 1093 | str      | str	w3, [x29, 44]                       | sw	x13, 44(x8)               |
| 1094 | str      | str	d0, [x29, 16]                       | fsd	f10, 16(x8)               |
| 1095 | str      | str	w0, [x29, 28]                       | sw	x10, 28(x8)               |
| 1096 | str      | str	w1, [x29, 52]                       | sw	x11, 52(x8)               |
| 1097 | str      | str	x0, [x29, 56]                       | sd	x10, 56(x8)               |
| 1098 | str      | str	x19, [sp, 16]                       | sd	x18, 16(x2)               |
| 1099 | str      | str	w0, [x29, 28]                       | sw	x10, 28(x8)               |
| 1100 | str      | str	d0, [x29, 40]                       | fsd	f10, 40(x8)               |
| 1101 | str      | str	wzr, [x29, 28]                       | sw	x0, 28(x8)               |
| 1102 | str      | str	d0, [x29, 40]                       | fsd	f10, 40(x8)               |
| 1103 | str      | str	d0, [x29, 40]                       | fsd	f10, 40(x8)               |
| 1104 | str      | str	d0, [x29, 40]                       | fsd	f10, 40(x8)               |
| 1105 | str      | str	d0, [x29, 40]                       | fsd	f10, 40(x8)               |
| 1106 | str      | str	d0, [x29, 40]                       | fsd	f10, 40(x8)               |
| 1107 | str      | str	d0, [x29, 40]                       | fsd	f10, 40(x8)               |
| 1108 | str      | str	d0, [x29, 40]                       | fsd	f10, 40(x8)               |
| 1109 | str      | str	d0, [x29, 40]                       | fsd	f10, 40(x8)               |
| 1110 | str      | str	d0, [x29, 32]                       | fsd	f10, 32(x8)               |
| 1111 | str      | str	d0, [x29, 24]                       | fsd	f10, 24(x8)               |
| 1112 | str      | str	w1, [x0]                       | sw	x11, 0(x10)               |
| 1113 | str      | str	w0, [x29, 68]                       | sw	x10, 68(x8)               |
| 1114 | str      | str	wzr, [x29, 36]                       | sw	x0, 36(x8)               |
| 1115 | str      | str	w2, [x1, x0]                       | add	s10, x10, x11 # dealt with reg offset               |
|      |          |                       | sw	x12, 0(s10)                                          |
| 1116 | str      | str	w0, [x29, 16]                       | sw	x10, 16(x8)               |
| 1117 | str      | str	w0, [x29, 20]                       | sw	x10, 20(x8)               |
| 1118 | str      | str	w0, [x29, 44]                       | sw	x10, 44(x8)               |
| 1119 | str      | str	w0, [x29, 72]                       | sw	x10, 72(x8)               |
| 1120 | str      | str	x1, [x29, 20040]                       | li	s10, 20040                                          |
|      |          |                       | add	s10, x26, x8 # dealt with reg offset               |
|      |          |                       | sd	x11, 0(s10)                                         |
| 1121 | str      | str	w0, [x29, 20]                       | sw	x10, 20(x8)               |
| 1122 | str      | str	w0, [x29, 24]                       | sw	x10, 24(x8)               |
| 1123 | str      | str	w0, [x29, 24]                       | sw	x10, 24(x8)               |
| 1124 | str      | str	w0, [x29, 20]                       | sw	x10, 20(x8)               |
| 1125 | str      | str	w0, [x29, 28]                       | sw	x10, 28(x8)               |
| 1126 | str      | str	w0, [x29, 28]                       | sw	x10, 28(x8)               |
| 1127 | str      | str	w0, [x29, 16]                       | sw	x10, 16(x8)               |
| 1128 | str      | str	w0, [x29, 20]                       | sw	x10, 20(x8)               |
| 1129 | str      | str	wzr, [x29, 16]                       | sw	x0, 16(x8)               |
| 1130 | str      | str	w0, [x29, 24]                       | sw	x10, 24(x8)               |
| 1131 | str      | str	w0, [x29, 16]                       | sw	x10, 16(x8)               |
| 1132 | str      | str	w0, [x29, 20]                       | sw	x10, 20(x8)               |
| 1133 | str      | str	w0, [x29, 16]                       | sw	x10, 16(x8)               |
| 1134 | str      | str	w0, [x29, 20]                       | sw	x10, 20(x8)               |
| 1135 | str      | str	x0, [x29, 56]                       | sd	x10, 56(x8)               |
| 1136 | str      | str	w0, [x29, 24]                       | sw	x10, 24(x8)               |
| 1137 | str      | str	w0, [x29, 28]                       | sw	x10, 28(x8)               |
| 1138 | str      | str	x0, [x29, 56]                       | sd	x10, 56(x8)               |
| 1139 | str      | str	x0, [x29, 48]                       | sd	x10, 48(x8)               |
| 1140 | str      | str	x0, [x29, 48]                       | sd	x10, 48(x8)               |
| 1141 | str      | str	x0, [x29, 32]                       | sd	x10, 32(x8)               |
| 1142 | str      | str	x0, [x29, 32]                       | sd	x10, 32(x8)               |
| 1143 | str      | str	x0, [x29, 40]                       | sd	x10, 40(x8)               |
| 1144 | str      | str	x0, [x29, 40]                       | sd	x10, 40(x8)               |
| 1145 | str      | str	w0, [x29, 28]                       | sw	x10, 28(x8)               |
| 1146 | str      | str	x2, [x1, 7256]                       | li	s10, 7256                                            |
|      |          |                       | add	s10, x26, x11 # dealt with reg offset               |
|      |          |                       | sd	x12, 0(s10)                                          |
| 1147 | str      | str	w0, [x29, 28]                       | sw	x10, 28(x8)               |
| 1148 | str      | str	w0, [x29, 44]                       | sw	x10, 44(x8)               |
| 1149 | str      | str	w0, [sp, 12]                       | sw	x10, 12(x2)               |
| 1150 | str      | str	w0, [x29, 68]                       | sw	x10, 68(x8)               |
| 1151 | str      | str	w0, [x29, 76]                       | sw	x10, 76(x8)               |
| 1152 | str      | str	x0, [x29, 24]                       | sd	x10, 24(x8)               |
| 1153 | str      | str	w2, [x29, 16]                       | sw	x12, 16(x8)               |
| 1154 | str      | str	w1, [x0]                       | sw	x11, 0(x10)               |
| 1155 | str      | str	w1, [x29, 20]                       | sw	x11, 20(x8)               |
| 1156 | str      | str	x0, [x29, 24]                       | sd	x10, 24(x8)               |
| 1157 | str      | str	w1, [x29, 20]                       | sw	x11, 20(x8)               |
| 1158 | str      | str	wzr, [x29, 44]                       | sw	x0, 44(x8)               |
| 1159 | str      | str	w0, [x29, 68]                       | sw	x10, 68(x8)               |
| 1160 | str      | str	w0, [x29, 40]                       | sw	x10, 40(x8)               |
| 1161 | str      | str	x0, [x29, 24]                       | sd	x10, 24(x8)               |
| 1162 | str      | str	w1, [x0]                       | sw	x11, 0(x10)               |
| 1163 | str      | str	w0, [x29, 44]                       | sw	x10, 44(x8)               |
| 1164 | str      | str	w0, [x29, 72]                       | sw	x10, 72(x8)               |
| 1165 | str      | str	w0, [x29, 44]                       | sw	x10, 44(x8)               |
| 1166 | strh     | strh	w2, [x1, x0]                       | add	s10, x10, x11 # dealt with reg offset               |
|      |          |                       | sh	x12, 0(s10)                                          |
| 1167 | sub      | sub	w1, w1, w0                       | subw	x11, x11, x10               |
| 1168 | sub      | sub	w1, w1, w0                       | subw	x11, x11, x10               |
| 1169 | sub      | sub	w1, w0, w1                       | subw	x11, x10, x11               |
| 1170 | sub      | sub	w0, w1, w0                       | subw	x10, x11, x10               |
| 1171 | sub      | sub	w1, w0, w1                       | subw	x11, x10, x11               |
| 1172 | sub      | sub	w1, w0, w1                       | subw	x11, x10, x11               |
| 1173 | sub      | sub	w1, w0, w1                       | subw	x11, x10, x11               |
| 1174 | sub      | sub	sp, sp, x16                       | sub	x2, x2, x27               |
| 1175 | sub      | sub	w1, w1, w0                       | subw	x11, x11, x10               |
| 1176 | sub      | sub	x1, x1, x0                       | sub	x11, x11, x10               |
| 1177 | sub      | sub	sp, sp, 32                       | addi	x2, x2, -32               |
| 1178 | sub      | sub	w1, w1, w0                       | subw	x11, x11, x10               |
| 1179 | sub      | sub	sp, sp, x16                       | sub	x2, x2, x27               |
| 1180 | sub      | sub	x1, x1, x0                       | sub	x11, x11, x10               |
| 1181 | sub      | sub	x1, x1, 1                       | addi	x11, x11, -1               |
| 1182 | sub      | sub	sp, sp, x0                       | sub	x2, x2, x10               |
| 1183 | sub      | sub	w0, w1, w0                       | subw	x10, x11, x10               |
| 1184 | sub      | sub	w0, w1, w0                       | subw	x10, x11, x10               |
| 1185 | sub      | sub	w1, w0, 1                       | addiw	x11, x10, -1               |
| 1186 | sub      | sub	x1, x0, x1                       | sub	x11, x10, x11               |
| 1187 | sub      | sub	sp, sp, x16                       | sub	x2, x2, x27               |
| 1188 | sub      | sub	x1, x1, 1                       | addi	x11, x11, -1               |
| 1189 | sub      | sub	sp, sp, x16                       | sub	x2, x2, x27               |
| 1190 | sub      | sub	w0, w1, w0                       | subw	x10, x11, x10               |
| 1191 | sub      | sub	x1, x0, x1                       | sub	x11, x10, x11               |
| 1192 | sub      | sub	sp, sp, x0                       | sub	x2, x2, x10               |
| 1193 | sub      | sub	w1, w1, w0                       | subw	x11, x11, x10               |
| 1194 | sub      | sub	w1, w0, w1                       | subw	x11, x10, x11               |
| 1195 | sub      | sub	sp, sp, 16                       | addi	x2, x2, -16               |
| 1196 | sxtw     | sxtw	x1, w0                       | sext.w	x11, x10               |
| 1197 | sxtw     | sxtw	x0, w0                       | sext.w	x10, x10               |
| 1198 | sxtw     | sxtw	x1, w0                       | sext.w	x11, x10               |
| 1199 | sxtw     | sxtw	x0, w0                       | sext.w	x10, x10               |
| 1200 | sxtw     | sxtw	x0, w0                       | sext.w	x10, x10               |
| 1201 | sxtw     | sxtw	x1, w0                       | sext.w	x11, x10               |
| 1202 | sxtw     | sxtw	x1, w0                       | sext.w	x11, x10               |
| 1203 | sxtw     | sxtw	x1, w0                       | sext.w	x11, x10               |
| 1204 | sxtw     | sxtw	x1, w0                       | sext.w	x11, x10               |
| 1205 | sxtw     | sxtw	x0, w0                       | sext.w	x10, x10               |
| 1206 | udiv     | udiv	w2, w0, w1                       | divuw	x12, x10, x11               |
| 1207 | udiv     | udiv	w2, w0, w1                       | divuw	x12, x10, x11               |
| 1208 | udiv     | udiv	w1, w1, w0                       | divuw	x11, x11, x10               |
| 1209 | udiv     | udiv	w1, w1, w0                       | divuw	x11, x11, x10               |