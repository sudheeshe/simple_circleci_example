# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        try:
                assert Add(2,3) == 6
                print("Add Function works correctly")

        except Exception as e:
                print('Add function failed')

if __name__ == '__main__':
        TestAdd()