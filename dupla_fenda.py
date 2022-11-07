from Neuraline.ComputationalPhysics.double_slit import DoubleSlit # importação da classe
double_slit = DoubleSlit() # instanciação do objeto da classe importada

result = double_slit.run( # execução da simulação física
    color_of_light='red', # coloração do raio de luz: red (vermelho) ou violet (violeta)
    type_of_opening='double_slit' # tipo de abertura: single_slit (fenda única), double_source (fonte dupla) ou double_slit (dupla fenda)
)
print(result) # exibição do resultado booleano de retorno