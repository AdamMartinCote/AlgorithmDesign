#include <cstring>
#include <iostream>

using namespace std; 

int main(int argc, char* argv[]) {
  char* fn = nullptr;
  bool show_p = false;
  bool show_t = false;

  for (int i=1; i<argc; i++) {
    if (!strcmp(argv[i], "-e")) {
      i++;
      fn = argv[i];
    }
    else if (!strcmp(argv[i], "-p")) {
      show_p = true;
    }
    else if (!strcmp(argv[i], "-t")) {
      show_t = true;
    }
    else if (!strcmp(argv[i], "-a")) {
      i++;
      if (!strcmp(argv[i], "brute")) {
	// todo
      }
      else if (!strcmp(argv[i], "seuil")) {
	// todo
      }
      else {
	cout << "Erreur: Algo inconnu" << endl;
	return -1;
      }
    }
  }

  if (show_p) {
    cout << "2.5" << endl; // Exemple de distance, ici une valeur bidon
  }
  if (show_t) {
    cout << "3.42" << endl; // Exemple de temps, ici une valeur bidon
  }
  
  return 0; 
} 
