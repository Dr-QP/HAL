#include <iostream>
#include <UnixSerial.h>
#include <boost/exception/diagnostic_information.hpp>

int main() {
  try
  {
    UnixSerial serial("/dev/tty");
  }
  catch(boost::exception &e)
  {
    std::cerr << "Boost exception caught...\n" << boost::diagnostic_information(e);
  }
  catch(...)
  {
    std::cerr << "Unknown exception caught...\n";
  }
}
