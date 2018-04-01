import os

def options(opt):
    opt.load(['compiler_cxx','gnu_dirs','boost','gmpxx','cxx17'])

def configure(conf):
    conf.load(['compiler_cxx','gnu_dirs','boost','gmpxx','cxx17'])
    conf.check_boost(lib='serialization system filesystem timer program_options chrono')

def build(bld):
    default_flags=['-Wall', '-Wextra', '-O3', '-D___MPACK_BUILD_WITH_GMP___']
    # default_flags=['-Wall', '-Wextra', '-g', '-ansi', '-D___MPACK_BUILD_WITH_GMP___']
    use_packages=['BOOST','gmpxx','cxx17']
    
    mpack_sources=['src/mpack/Rpotrf.cpp',
                   'src/mpack/Rgemm.cpp',
                   'src/mpack/Rorgql.cpp',
                   'src/mpack/Rgetf2.cpp',
                   'src/mpack/Rsterf.cpp',
                   'src/mpack/RgemmParallel.cpp',
                   'src/mpack/Rlarft.cpp',
                   'src/mpack/Rorgtr.cpp',
                   'src/mpack/Rlartg.cpp',
                   'src/mpack/Rorgqr.cpp',
                   'src/mpack/Rlapy2.cpp',
                   'src/mpack/Rpotf2.cpp',
                   'src/mpack/Rgetrf.cpp',
                   'src/mpack/iMlaenv.cpp',
                   'src/mpack/Rsytd2.cpp',
                   'src/mpack/Rger.cpp',
                   'src/mpack/Rlamch.cpp',
                   'src/mpack/Rtrsv.cpp',
                   'src/mpack/Rlae2.cpp',
                   'src/mpack/Rorg2r.cpp',
                   'src/mpack/Rswap.cpp',
                   'src/mpack/Rtrsm.cpp',
                   'src/mpack/Rrot.cpp',
                   'src/mpack/Rgemv.cpp',
                   'src/mpack/iRamax.cpp',
                   'src/mpack/Rlarf.cpp',
                   'src/mpack/Rsyr2k.cpp',
                   'src/mpack/Rsteqr.cpp',
                   'src/mpack/Rlatrd.cpp',
                   'src/mpack/Rlaev2.cpp',
                   'src/mpack/Mxerbla.cpp',
                   'src/mpack/Rnrm2.cpp',
                   'src/mpack/Rscal.cpp',
                   'src/mpack/Rsyrk.cpp',
                   'src/mpack/Rsyr2.cpp',
                   'src/mpack/Rcopy.cpp',
                   'src/mpack/Rrotg.cpp',
                   'src/mpack/Rlasr.cpp',
                   'src/mpack/Rtrmv.cpp',
                   'src/mpack/Rlansy.cpp',
                   'src/mpack/Rpotf2Stabilized.cpp',
                   'src/mpack/Rtrmm.cpp',
                   'src/mpack/Raxpy.cpp',
                   'src/mpack/Rlaswp.cpp',
                   'src/mpack/Rsytrd.cpp',
                   'src/mpack/Rlaset.cpp',
                   'src/mpack/Rlarfb.cpp',
                   'src/mpack/Rsymv.cpp',
                   'src/mpack/Rsyev.cpp',
                   'src/mpack/Rorg2l.cpp',
                   'src/mpack/Rlascl.cpp',
                   'src/mpack/Rlasrt.cpp',
                   'src/mpack/RpotrfStabilized.cpp',
                   'src/mpack/Rdot.cpp',
                   'src/mpack/Mlsame.cpp',
                   'src/mpack/Rgetrs.cpp',
                   'src/mpack/Rlanst.cpp',
                   'src/mpack/Rlassq.cpp',
                   'src/mpack/Rlarfg.cpp']

    bld.stlib(source=mpack_sources,
              target='mpack',
              name='mpack_st',
              includes=['src/mpack'],
              cxxflags=default_flags,
              install_path=bld.env.LIBDIR,
              use=use_packages
              )

    # Main executable
    bld.program(source=['src/main.cxx',
                        'src/SDP_Solver_Parameters/ostream.cxx',
                        'src/solve/solve.cxx',
                        'src/solve/SDP_Solver/IO.cxx',
                        'src/solve/SDP_Solver/SDPSolver.cxx',
                        'src/solve/SDP_Solver_Terminate_Reason/ostream.cxx',
                        'src/solve/Block_Diagonal_Matrix/block_diagonal_matrix_multiply.cxx',
                        'src/solve/Block_Diagonal_Matrix/block_diagonal_matrix_scale_multiply_add.cxx',
                        'src/solve/Block_Diagonal_Matrix/block_matrix_lower_triangular_solve.cxx',
                        'src/solve/Block_Diagonal_Matrix/block_matrix_lower_triangular_transpose_solve.cxx',
                        'src/solve/Block_Diagonal_Matrix/block_matrix_solve_with_cholesky.cxx',
                        'src/solve/Block_Diagonal_Matrix/cholesky_decomposition.cxx',
                        'src/solve/Block_Diagonal_Matrix/cholesky_decomposition_stabilized.cxx',
                        'src/solve/Block_Diagonal_Matrix/frobenius_product_of_sums.cxx',
                        'src/solve/Block_Diagonal_Matrix/frobenius_product_symmetric.cxx',
                        'src/solve/Block_Diagonal_Matrix/lower_triangular_inverse_congruence.cxx',
                        'src/solve/Block_Diagonal_Matrix/min_eigenvalue.cxx',
                        'src/solve/Block_Diagonal_Matrix/ostream.cxx',
                        'src/solve/Matrix/cholesky_decomposition.cxx',
                        'src/solve/Matrix/cholesky_decomposition_stabilized.cxx',
                        'src/solve/Matrix/frobenius_product_of_sums.cxx',
                        'src/solve/Matrix/frobenius_product_symmetric.cxx',
                        'src/solve/Matrix/lower_triangular_inverse_congruence.cxx',
                        'src/solve/Matrix/lower_triangular_solve.cxx',
                        'src/solve/Matrix/lower_triangular_transpose_solve.cxx',
                        'src/solve/Matrix/LU_decomposition.cxx',
                        'src/solve/Matrix/matrix_eigenvalues.cxx',
                        'src/solve/Matrix/matrix_scale_multiply_add.cxx',
                        'src/solve/Matrix/matrix_solve_with_cholesky.cxx',
                        'src/solve/Matrix/matrix_square_into_block.cxx',
                        'src/solve/Matrix/min_eigenvalue.cxx',
                        'src/solve/Matrix/ostream.cxx',
                        'src/solve/Matrix/solve_with_LU_decomposition.cxx',
                        'src/solve/Matrix/vector_scale_matrix_multiply_add.cxx',
                        'src/solve/Matrix/vector_scale_matrix_multiply_transpose_add.cxx',
                        'src/solve/read_bootstrap_sdp/read_bootstrap_sdp.cxx',
                        'src/solve/read_bootstrap_sdp/parse_vector.cxx',
                        'src/solve/read_bootstrap_sdp/parse_Real.cxx',
                        'src/solve/read_bootstrap_sdp/parse_polynomial_vector_matrix.cxx',
                        'src/solve/read_bootstrap_sdp/bootstrap_SDP/bootstrap_SDP.cxx',
                        'src/solve/read_bootstrap_sdp/bootstrap_SDP/dual_constraint_group_from_pol_vec_mat/dual_constraint_group_from_pol_vec_mat.cxx',
                        'src/solve/read_bootstrap_sdp/bootstrap_SDP/dual_constraint_group_from_pol_vec_mat/sample_bilinear_basis.cxx',
                        'src/solve/read_bootstrap_sdp/bootstrap_SDP/sdp_from_dual_constraint_groups.cxx'],
                target='sdpb',
                includes=['src/mpack'],
                cxxflags=default_flags,
                rpath=[bld.env.LIBDIR],
                use=use_packages + ['mpack_st'],
                )
