#include <iostream>
#include <ctime>

using namespace std;

int main(){
	time_t t = time(NULL);
	tm *tempoInicial = localtime(&t);

	// int ano = 1900 + tempoInicial->tm_year;
	// int mes = 1 + tempoInicial->tm_mon;
	// int dia = tempoInicial->tm_mday;
	int hora = tempoInicial->tm_hour;
	int minuto = tempoInicial->tm_min;
	int segundo = tempoInicial->tm_sec;
	
	int total = 0;
	int totalRange = 10000;
	for(int i = 0; i < totalRange; i++){
		total += i;
		if(i == totalRange - 1){
			cout << "--Soma finalizada--";
		}
	}

	tm *tempoFinal = localtime(&t);
	int hora = tempoFinal->tm_hour;
	int minuto = tempoFinal->tm_min;
	int segundo = tempoFinal->tm_sec;

	//cout << "Nós estamos em : " << dia << "/"<<mes<<"/"<<ano<< endl;
	cout << "E agora são : "<<hora<<":"<<minuto<<":"<<segundo<<endl	;
	return 0;
}