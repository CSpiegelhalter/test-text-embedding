from tte.DataLoaderV1 import Create_dataloader_v1
import os
def main():

    here = os.path.dirname(__file__)  # folder containing main.py
    path = os.path.join(here, "shakespear.txt")

    with open(path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    dataloader = Create_dataloader_v1(
        raw_text, batch_size=1, max_length=4, stride=1, shuffle=False
    )

    data_iter = iter(dataloader)
    first_batch = next(data_iter)
    print(first_batch)

if __name__ == '__main__':
    main()