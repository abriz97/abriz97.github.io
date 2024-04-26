import yaml

with open('data/PUBLICATIONS.yml', 'r') as file:
    publications = yaml.safe_load(file)

# write a markdown table which contains,
# for each publications,
# the first three authors,
# the title with a link to the publication,
# and the publication year in brackets ()

with open('pages/PUBLICATIONS.md', 'w') as md_file:
    md_file.write('# Publications\n\n')
    md_file.write('| Authors | Title | Year |\n')
    md_file.write('| --- | --- | --- |\n')
    for pub in publications["works"]:
        authors = ', '.join(pub['authors'][:3])
        title = f"[{pub['title']['value']}]({pub['url']})"
        year = f"({pub['publicationDate']['year']})"
        md_file.write(f"| {authors} | {title} | {year} |\n")
