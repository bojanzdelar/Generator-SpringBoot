export interface TableColumn {
  key: string;
  name: string;
  display?: DisplayFn;
  footer?: FooterAgg;
}

interface DisplayFn {
  (row: any): string;
}

interface FooterAgg {
  (data: any, key: string): any;
}
