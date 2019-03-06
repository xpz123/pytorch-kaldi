export KALDI_ROOT=/workspace/shaogao/kaldi
PATH=$PATH:$KALDI_ROOT/tools/openfst
PATH=$PATH:$KALDI_ROOT/src/featbin
PATH=$PATH:$KALDI_ROOT/src/gmmbin
PATH=$PATH:$KALDI_ROOT/src/bin
PATH=$PATH:$KALDI_ROOT//src/nnetbin
PATH=$PATH:$KALDI_ROOT/src/chainbin
export PATH
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$KALDI_ROOT/tools/OpenBLAS:$KALDI_ROOT/tools/openfst-1.6.7/lib
export LD_LIBRARY_PATH
