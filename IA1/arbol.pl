%Hombres
hombre('Arthur').
hombre('Bill').
hombre('George').
hombre('Ron').
hombre('Louis').
hombre('Fred').
hombre('Hugo').
hombre('Teddy').
hombre('Percy').
hombre('Harry').
hombre('James').
hombre('Albus').

%Mujeres
mujer('Molly prewett').
mujer('Fleur').
mujer('Angelina').
mujer('Hermione').
mujer('Victoire').
mujer('Dominique').
mujer('Roxanne').
mujer('Rose').
mujer('Audrey').
mujer('Ginny').
mujer('Lucy').
mujer('Molly').
mujer('Lily').


%nivel_1_2
:- discontiguous padrede/2, madrede/2.
padrede('Arthur','Bill').
madrede('Molly prewett','Bill').
padrede('Arthur','Percy').
madrede('Molly prewett','Percy').
padrede('Arthur','George').
madrede('Molly prewett','George').
padrede('Arthur','Ginny').
madrede('Molly prewett','Ginny').
padrede('Arthur','Ron').
madrede('Molly prewett','Ron').

%nivel_2_3
    %Bill
:- discontiguous padrede/2, madrede/2.
padrede('Bill','Victoire').
madrede('Fleur','Victoire').
padrede('Bill','Dominique').
madrede('Fleur','Dominique').
padrede('Bill','Lois').
madrede('Fleur','Loise').
    %Percy
padrede('Percy','Lucy').
madrede('Audrey','Lucy').
padrede('Percy','Molly').
madrede('Audrey','Molly').
    %George
padrede('George','Fred').
madrede('Angelina','Fred').
padrede('George','Roxanne').
madrede('Angelina','Roxanne').
    %Ginny
padrede('Harry','James').
madrede('Ginny','James').
padrede('Harry','Lily').
madrede('Ginny','Lily').
padrede('Harry','Albus').
madrede('Ginny','Albus').
    %Ron
padrede('Ron','Hugo').
madrede('Hermione','Hugo').
padrede('Ron','Rose').
madrede('Hermione','Rose').

%nivel_4
madrede('Victoire','Teddy').

%Conexiones
bisabuelo(X, Y) :- padrede(X, Z), abuelo(Z, Y).
bisabuela(X, Y) :- madrede(X, Z), abuela(Z, Y).
abuelo(X, Y) :- padrede(X, Z), padrede(Z, Y).
abuela(X, Y) :- madrede(X, Z), padrede(Z, Y).
padre(X, Y) :- padrede(X, Y).
madre(X, Y) :- madrede(X, Y).

padre_nivel3_4(X, Y) :- padrede(X, Z), padrede(Z, W), padrede(W, Y).
madre_nivel3_4(X, Y) :- madrede(X, Z), padrede(Z, W), padrede(W, Y).

%Hijo_de
hijo_de(X, Y) :- padrede(Y, X).
hijo_de(X, Y) :- madrede(Y, X).

%Hija_de
hija_de(X, Y) :- padrede(Y, X).
hija_de(X, Y) :- madrede(Y, X).

%Hermano_de
hermano_de(X, Y) :- 
    hombre(X),              % X es un hombre
    padrede(Z, X),          % Z es el padre de X
    padrede(Z, Y),          % Z es también el padre de Y
    X \= Y.                 % X no es igual a Y (para evitar a sí mismo)

%Hermana_de
hermana_de(X, Y) :- 
    mujer(X),               % X es una mujer
    padrede(Z, X),          % Z es el padre de X
    padrede(Z, Y),          % Z es también el padre de Y
    X \= Y.                 % X no es igual a Y

%Tio_de
tio_de(X, Y) :- 
    hombre(X),              % X es un hombre
    hermano_de(X, Z),       % X es hermano de Z
    padrede(Z, Y).          % Z es el padre de Y

%Tia_de
tia_de(X, Y) :- 
    mujer(X),               % X es una mujer
    hermana_de(X, Z),       % X es hermana de Z
    padrede(Z, Y).          % Z es el padre de Y

%Primo_de
primo_de(X, Y) :- 
    hombre(X),              % X es un hombre
    padrede(Z, X),          % Z es el padre de X
    tio_de(Z, Y).           % Z es tío de Y

%Prima_de
prima_de(X, Y) :- 
    mujer(X),               % X es una mujer
    padrede(Z, X),          % Z es el padre de X
    tia_de(Z, Y).           % Z es tía de Y

%Sobrino_de
sobrino_de(X, Y) :- 
    hombre(X),              % X es un hombre
    tio_de(Y, X).           % Y es tío de X

%Sobrina_de
sobrina_de(X, Y) :- 
    mujer(X),               % X es una mujer
    tia_de(Y, X).           % Y es tía de X

%Nieta_de
nieta_de(X, Y) :- 
    mujer(X),               % X es una mujer
    abuela(Y, X).           % Y es abuela de X

%Nieto_de
nieto_de(X, Y) :- 
    hombre(X),              % X es un hombre
    abuelo(Y, X).           % Y es abuelo de X


/* QUERIES DE PRUEBA
    hermano_de(X, 'Ron').
    tio_de(X, 'Teddy').
    primo_de(X, 'James').
    nieto_de(X, 'Molly prewett').
*/