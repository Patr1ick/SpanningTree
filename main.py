from argparse import ArgumentParser
from src.spanningtree.spanningtree import SpanningTree
from src.spanningtree.fileparser import FileParser


if __name__ == '__main__':

    # Arguments for commandline
    parser = ArgumentParser()

    parser.add_argument('-f', '--file', dest='filename',
                        help='File for reading the data for the spanning tree')
    parser.add_argument('-o', '--out', dest='outfile',
                        help='File for writing the output of the spanning tree')
    parser.add_argument('-m', '--min', dest='min',
                        help='Minimum value that the nodes have ti reach to stop the algorithm', default=2)
    parser.add_argument('-q', '--quiet', dest='quiet',
                        help='No output to the terminal except the final spanning tree', action='store_true')

    args = parser.parse_args()

    if args.filename != None or args.filename != '':

        # Parse the file
        fp = FileParser(args.filename)
        nodes, edges = fp.parse(return_value=True)

        # Generate paths
        sp = SpanningTree(nodes, edges, int(args.min), quiet=args.quiet)
        sp.gen()

        # Output
        if args.outfile is not None:
            print(f"Ouput in {args.outfile}")
            f = open(args.outfile, "w")
            for n in sp.nodes:
                if n.next_node == 0:
                    f.write(f"{n.name} (Root)")
                else:
                    f.write(f"{n.name} - {n.next_node} ({n.cost})")
                f.write("\n")
            f.close()
        else:
            print("\n--- Output ---")
            for n in sp.nodes:
                if n.next_node == 0:
                    print(f"{n.name} (Root)")
                else:
                    print(f"{n.name} - {n.next_node} ({n.cost})")
    else:
        raise ValueError('No file name was specified for the input in the arguments.')