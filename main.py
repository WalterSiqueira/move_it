import click
import os

@click.group()
def cli():
    pass

@cli.command()
@click.option('--path', prompt='enter the path to the source folder', help='/path/to/your/folder')
@click.option('--dest', prompt='enter the path to the destination folder', help='/path/to/your/folder')
@click.option('--ext', prompt='enter the file extension please!', help='ex: .mp3,.mp4,.pdf')
def move(path, ext, dest):
    is_valid = os.path.exists(path)
    if is_valid == True :
        path_contents = os.listdir(path)
        for content in path_contents :
            file_validation = content.endswith(ext)
            if file_validation == True :
                match_files = content
                command = f"mv {path}/*{ext} {dest}"
                status = os.system(command)
                if status == 0:
                    print("moved successfully")
                else :
                    print("operation failed with the status of", status)
            else:
                print("no match found")
    else :
        print("Error: invalid path!")
    

if __name__ == '__main__':
    cli()
