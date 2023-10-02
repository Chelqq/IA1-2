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


/*Reglas para relaciones de padre y madre*/
padre(Padre, Hijo) :- padrede(Padre, Hijo).
madre(Madre, Hijo) :- madrede(Madre, Hijo).

/*Regla para hermano*/
hermano(X, Y) :-
    hombre(X),       % X es un hombre
    padrede(Z, X),   % Z es el padre de X
    padrede(Z, Y),   % Z es el padre de Y (mismo padre)
    X \= Y.          % X no es igual a Y (evita que alguien sea su propio hermano)

hermana(X, Y) :-
    mujer(X),        % X es una mujer
    madrede(Z, X),   % Z es la madre de X
    madrede(Z, Y),   % Z es la madre de Y (misma madre)
    X \= Y.          % X no es igual a Y (evita que alguien sea su propia hermana)


/*Regla para esposo y esposa*/
esposo(X, Y) :- padrede(X, Hijo), madrede(Y, Hijo).
esposa(X, Y) :- madrede(X, Hijo), padrede(Y, Hijo).


/*Regla para suegro y suegra*/
suegro(Suegro, Yerno) :-
    padre(Suegro, Hija),
    esposa(Hija, Yerno).

suegra(Suegra, Yerno) :-
    madre(Suegra, Hija),
    esposa(Hija, Yerno).

/*Regla para yerno y nuera*/
yerno(X, Y) :-
    hombre(X),           % X es un hombre.
    esposo(X, Z),        % X está casado con Z.
    madrede(Z, Y).       % Z es la madre de Y.

nuera(X, Y) :-
    mujer(X),            % X es una mujer.
    esposa(X, Z),        % X está casada con Z.
    padrede(Z, Y).       % Z es el padre de Y.


/*Regla para cunado y cunada*/
cunado(cunado, Persona) :-
    esposo(cunado, Hermana),
    hermano(Persona, Hermana).

cunada(cunada, Persona) :-
    esposa(cunada, Hermano),
    hermana(Persona, Hermano).

/*Regla para abuelo y abuela*/
abuelo(X, Y) :-
    hombre(X),
    padrede(X, Z),
    padrede(Z, Y).

abuela(X, Y) :-
    mujer(X),
    madrede(X, Z),
    madrede(Z, Y).

nieto(X, Y) :-
    hombre(X),
    (abuelo(Y, X); abuela(Y, X)).

nieta(X, Y) :-
    mujer(X),
    (abuelo(Y, X); abuela(Y, X)).

tio(X, Y) :-
    hombre(X),
    (hermano(X, Z), (padrede(Z, Y); madrede(Z, Y))).

tia(X, Y) :-
    mujer(X),
    (hermana(X, Z), (padrede(Z, Y); madrede(Z, Y))).

primo(X, Y) :-
    hombre(X),
    (tio(Z, X), (padrede(Z, Y); madrede(Z, Y))).

prima(X, Y) :-
    mujer(X),
    (tia(Z, X), (padrede(Z, Y); madrede(Z, Y))).


/*
Queries de prueba:
hermano(X, 'Bill').
hermana(X, 'Bill').
esposo(Esposo, Esposa).     parejas de esposos
esposa(X, 'Ron').
suegro(Suegro, 'Harry').
yerno(X,Y).
yerno(X,'Bill')
abuela(X, 'James').
primo(X, 'Rose').


*/