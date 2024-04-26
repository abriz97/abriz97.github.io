import yaml

with open('data/PUBLICATIONS.yml', 'r') as file:
    publications = yaml.safe_load(file)

# write a markdown table which contains,
# for each publications,
# the first three authors,
# the title with a link to the publication,
# the journal name, in italics if any
# and the publication year in brackets ()
get_first_authors = lambda pub: ', '.join(pub['authors'][:3])
get_title = lambda pub: f"[{pub['title']['value']}]({pub['url']})"
get_journal = lambda pub: pub["journalTitle"] if pub["journalTitle"] else "preprint"
get_year = lambda pub: f"({pub['publicationDate']['year']})"

with open('pages/PUBLICATIONS.md', 'w') as md_file:
    md_file.write('| Authors | Title | Journal | Year |\n')
    md_file.write('| --- | --- | --- | --- |\n')
    for pub in publications["works"]:
        authors = get_first_authors(pub)
        title = get_title(pub)
        year = get_year(pub)
        journal_name = get_journal(pub)
        print(f"| {authors} | {title} | {journal_name} | {year} |")
        md_file.write(f"| {authors} | {title} | {journal_name} | {year} |\n")

