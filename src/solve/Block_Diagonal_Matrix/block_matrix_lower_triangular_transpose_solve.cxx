#include "../Block_Diagonal_Matrix.hxx"

// v := L^{-T} v, where L is lower-triangular
void block_matrix_lower_triangular_transpose_solve(Block_Diagonal_Matrix &L,
                                                   Vector &v)
{
  for(size_t b = 0; b < L.blocks.size(); b++)
    {
      lower_triangular_transpose_solve(
        L.blocks[b], &v[L.block_start_indices[b]], 1, v.size());
    }
}
