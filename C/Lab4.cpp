#include <iostream>
using namespace std;
int main()
{
	string option;
	option = "Si"; //Opción para saber si se repite o no
	int entrada;

	bool a = false;
	bool b = false;
	bool c =false;
	bool d = false;
	cout<<"Ingresa 1 si la maquina envio alerta o 0 si no\n";
	while(option == "Si")
	{
		for(int i = 0; i<4; i++) //Ingreso de datos
		{
			cout<<"\nIngrese datos de la maquina ["<<i+1<<"]: ";
			cin>>entrada;
			switch (i)
			{
				case 0:
					if(entrada == 1)
					{
						a = true;
					}
					else
					{
						a = false;
					}
				case 1:
					if(entrada == 1)
					{
						b = true;
					}
					else
					{
						b = false;
					}
				case 2:
					if(entrada == 1)
					{
						c = true;
					}
					else
					{
						c = false;
					}
				case 3:
					if(entrada == 1)
					{
						d = true;
					}
					else
					{
						d = false;
					}
			}
		}
		if((a==true)||(c==true)) //maquiana S1 alerta
		{
			cout<<"\n S1 esta en peligro";
		}
		else
		{
			cout<<"\n S1 no esta en peligro";
		}
		if((c && (a || b || d))||(a && b &&  d)) //maquiana S2 alerta
		{
			cout<<"\n S2 esta en peligro";
		}
		else
		{
			cout<<"\n S2 no esta en peligro";
		}
		if((a==true)||(d && (c || b))) //maquiana S3 alerta
		{
			cout<<"\n S3 esta en peligro";
		}
		else
		{
			cout<<"\n S3 no esta en peligro";
		}
	}
	
	
	return 0;
}
