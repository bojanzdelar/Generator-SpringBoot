import { Component, EventEmitter, Input, OnInit, Output } from "@angular/core";
import { TableColumn } from "@models/table-column";
import * as _ from "lodash";

@Component({
  selector: "app-table",
  templateUrl: "./table.component.html",
  styleUrls: ["./table.component.css"],
})
export class TableComponent implements OnInit {
  @Input()
  title: string = "Table";

  @Input()
  columns: TableColumn[] = [];

  @Input()
  elements: any[] = [];

  @Input()
  editable: boolean = true;

  @Input()
  deletable: boolean = true;

  @Output()
  edit: EventEmitter<any> = new EventEmitter();

  @Output()
  delete: EventEmitter<any> = new EventEmitter();

  constructor() {}

  ngOnInit(): void {}

  emitEdit(i: any, v: any) {
    this.edit.emit({ index: i, value: { ...v } });
  }

  emitDelete(i: any, v: any) {
    this.delete.emit({ index: i, value: { ...v } });
  }

  get(row: any, key: string) {
    return _.get(row, key);
  }

  footerExists(): boolean {
    return this.columns.some((c: TableColumn) => c.footer !== undefined);
  }

  sort(column: string): void {
    this.elements.sort((a: any, b: any) => {
      if (a[column] === undefined) {
        return -1;
      }

      if (a[column] < b[column]) {
        return -1;
      } else if (a[column] > b[column]) {
        return 1;
      } else {
        return 0;
      }
    });
  }
}
