#include "../kabuki.press/client.inl"

int main(const char** args, int arg_count) {
  return kabuki::press::Client(args, arg_count).Run();
}
