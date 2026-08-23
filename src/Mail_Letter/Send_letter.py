with open("/Users/<username>/PycharmProjects/<folder>/src/Mail_Letter/Names","r") as f1:
    names = f1.readlines()
    # for line in content:
    #     print(line.strip())

with open("/Users/<username>/PycharmProjects/<folder>/src/Mail_Letter/letter","r") as f2:
    content1 = f2.read()
    for line in names:
        stripped_name = line.strip()
        new_content=content1.replace("[name]",stripped_name)
        print(new_content)
        with open(f"letter_for_{line}.docx","w") as f3:
            f3.write(new_content)
    # print(content1)
    # for line in content1:
