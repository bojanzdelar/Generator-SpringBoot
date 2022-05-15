import { Directive, Input, TemplateRef, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[appEmptyTable]',
})
export class EmptyTableDirective {
  @Input()
  set appEmptyTable(value: any) {
    this.viewContainer.clear();
    if (value != undefined && value.length != undefined && value.length > 0) {
      this.viewContainer.createEmbeddedView(this.templateRef);
    } else if (this.appEmptyTableMessage != undefined) {
      this.viewContainer.createEmbeddedView(this.appEmptyTableMessage);
    }
  }

  @Input()
  appEmptyTableMessage: TemplateRef<any> | undefined = undefined;

  constructor(
    private templateRef: TemplateRef<any>,
    private viewContainer: ViewContainerRef
  ) {}
}
